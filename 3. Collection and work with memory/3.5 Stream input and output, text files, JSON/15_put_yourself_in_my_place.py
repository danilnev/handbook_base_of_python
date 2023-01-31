import json
import sys

with open(file='scoring.json', encoding='utf-8') as system:
    system = json.load(system)
answers = [line.rstrip() for line in sys.stdin.readlines()]
count = 0
points = 0
for group in system:
    tests = 0
    rights = 0
    for test in group['tests']:
        if answers[count] == test['pattern']:
            rights += 1
        tests += 1
        count += 1
    if tests == rights:
        points += group['points']
    else:
        points += group['points'] * (rights / tests)
print(int(points))
