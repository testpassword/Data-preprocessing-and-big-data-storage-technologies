import csv
import statistics
from collections import defaultdict


def read_to_dict(file) -> dict:
    return [
        {k: v for k, v in row.items()}
        for row in csv.DictReader(file, delimiter=';', skipinitialspace=True)
    ]


# Build a column chart for the number of cases in 2010-2018 for all countries. Compare your charts with the chart below and determine which country the graph below is built for 
with open('task1_demo.csv', mode='r', encoding='utf-8-sig') as f:
    stats = defaultdict(list)
    for it in read_to_dict(f):
        stats[it['Cname']] += [it]
        del it['Cname']
country = list({
    k: v for k, v in {
        k: max(v, key=lambda it: int(it['Number of cases'])) 
        for k, v in stats.items()
    }.items() if int(v['Year']) == 2017
}.keys())[0]
print(f'{country=}')


# Find the following statistical characterictics for Australia for the years 2010 — 2018.
with open('task1_demo.csv', mode='r', encoding='utf-8-sig') as f:
    stats = [
        int(it['Number of cases']) for it in read_to_dict(f) 
        if it['Cname'] == 'Australia' and int(it['Year']) in range(2010, 2018 + 1)
    ]
median = round(statistics.median(stats))
variance = round(statistics.variance(stats))
print(f'{median=} , {variance=}')


# Find the total number of mumps incedence for Europe for the whole period of time.
with open('task3_demo_regions.csv', mode='r', encoding='utf-8-sig') as rf:
    eu_countries = [it['Cname'] for it in read_to_dict(rf) if it['Region'] == 'Europe']
with open('task3_demo_countries.csv', mode='r', encoding='utf-8-sig') as cf:
    num_of_incedence = [
        int(it['Number of cases']) for it in read_to_dict(cf)
        if it['Cname'] in eu_countries
    ]
total = sum(num_of_incedence)
print(f'{total=}')
