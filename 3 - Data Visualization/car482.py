#!python3
from collections import namedtuple
import csv
import re

Record = namedtuple('Record', ['line_type', 'line', 'car'])
COUNTERS = {
    'SINGLE': {
        'count': 0,
        'direction_is_swapped': False
    }, 
    'INTERRUPT': {
        'count': 0,
        'direction_is_swapped': False
    },
    'DOUBLE': {
        'count': 0,
        'direction_is_swapped': False
    }
}
records = []
with open('car482.csv') as f:
    line_count = 0
    for row in csv.reader(f, delimiter=','):
        if line_count != 0:
            records = records + [Record(line_type=row[0], line=int(row[1]), car=int(row[2]))]
        line_count += 1
for i, it in enumerate(records):
    if it.car > 1000:
        records[i] = it._replace(car=((records[i - 1].car + records[i + 1].car) / 2))
for r in records:
    counter = COUNTERS[r.line_type]
    if r.car > r.line and counter['direction_is_swapped'] == False:
        counter['count'] = counter['count'] + 1
        counter['direction_is_swapped'] = True
    if r.car < r.line and counter['direction_is_swapped'] == True:
        counter['count'] = counter['count'] + 1
        counter['direction_is_swapped'] = False
print({k: v['count'] for k, v in COUNTERS.items()})


