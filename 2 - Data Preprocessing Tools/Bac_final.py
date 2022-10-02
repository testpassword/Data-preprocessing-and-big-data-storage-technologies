#!python3
from collections import namedtuple
import csv
from statistics import mean
from itertools import groupby
from operator import itemgetter

Record = namedtuple('Record', ['group', 'student_id', 'tasks', 'essay'])
records = []
with open('Bac_final.csv') as f:
    line_count = 0
    for row in csv.reader(f, delimiter=';'):
        row = row[0].split(';')
        if line_count != 0:
            records = records + [Record(group=row[0], student_id=row[1], tasks=[int(v) for v in row[2:-1]], essay=int(row[-1]))]
        line_count += 1
res1 = (
    round(
        mean(
            [r.tasks[7-1] for r in records if r.group.startswith('N')]
            )
        )
    )
print(f'What is the average score in task 7 for all students of the Faculty of Secure Information Technologies (the first letter in the group name is N)? {res1=}')
candidates = [(r.group, r.tasks[1-1]) for r in records if r.group.startswith('T')]
sortkeyfn = itemgetter(0)
candidates.sort(key=sortkeyfn)
res2 = (
    sorted(
        {key: round(
            mean(
                list(v[1] for v in valuesiter)
                )
            ) for key, valuesiter in groupby(candidates, key=sortkeyfn)
        }.items(), 
        key=lambda it: it[1], 
        reverse=True
        )[0]
    )[0]
print(f'What group of the Faculty of Food Biotechnologies and Engineerings (the first letter in the group name is T) coped the best way with the exercise 1 (i.e. has got the maximum average score for the task 1)? (Type the group name starting from the capital letter.) {res2=}')
res3 = (
    len([it for it in records if it.essay == 100])
)
print(f'How many students have got 100 points for the essay (rounding to the nearest whole number is applied)? {res3=}')