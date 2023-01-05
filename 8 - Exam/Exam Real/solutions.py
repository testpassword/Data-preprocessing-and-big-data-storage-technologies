import csv
import statistics
from collections import defaultdict


def read_file_to_dict(filepath: str) -> dict:
    with open(filepath, mode='r') as file:
        return [
            {k: v for k, v in row.items()}
            for row in csv.DictReader(file, delimiter=',', skipinitialspace=True)
        ]


# Calculate the total electricity consumption in the year 2003 in the Northwestern federal district
electricity_consumption = read_file_to_dict('ITMOUniversity+DTSTPR+fall_2021_ITMO+type@asset+block@СубъектыРФ_en.csv')
districts = read_file_to_dict('ITMOUniversity+DTSTPR+fall_2021_ITMO+type@asset+block@РегионыРФ_en.csv')
nw_districts = [it['District'] for it in districts if it['Fededal District'] == 'Northwestern']
nw_consumption2003 = sum([float(it['2003']) for it in electricity_consumption if it['District'] in nw_districts])
print(f'{nw_consumption2003=}')


# Calculate the total electricity consumption from 2000 until 2010 in the Northwestern federal district
nw_consumption200x = sum([
        sum({float(v) for k, v in it.items() if k.isnumeric() and int(k) in range(2000, 2010 + 1)})
        for it in electricity_consumption if it['District'] in nw_districts
    ]
)
print(f'{nw_consumption200x=}')