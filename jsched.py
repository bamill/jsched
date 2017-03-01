#!/usr/bin/python3

import random

# 35 hours a week for 7 hours/5 days a week
# 5 areas: Consultation, Intervention, Assessment, Meetings, Documentation
# No more than 40% in any one area, no less than 10% in any one area
# Consultation and intervention should be around 10% each
# Supervision is always 2 hours on Fridays

areas = {'Supervision': .057143, 'Consultation': .1, 'Intervention': .1, 'Assessment': 0, 'Meetings': 0, 'Documentation': 0}

def allotments(a):
    l = ['Assessment', 'Meetings', 'Documentation']
    for area in l:
        a[area] = random.randrange(100000, 400000, 14286) / 1000000
    if sum(a.values()) > 1 or max(a.values()) > .4:
        allotments(a)
    tmp = {i: a[i] for i in l}
    m = min(tmp, key=tmp.get)
    a[m] = a[m] + (1 - sum(a.values()))
    return a

allotments(areas)
hours = {i: round(areas[i] * 35, 2) for i in areas.keys()}
hours_m = {i: hours[i] for i in hours.keys() if i is not 'Supervision'}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
week = {d: 7 for d in days}
week['Friday'] = 5
print()
for d in days:
    print(d + ":\n")
    if d is 'Friday':
        print('Supervision: 2 hours')
    while(week[d] > 0):
        for a in hours_m:
            if hours_m[a] != 0 and hours_m[a] < week[d]:
                print(a + ': ' + str(hours_m[a]) + ' hour(s)')
                week[d] = week[d] - hours_m[a]
                hours_m[a] = 0
            elif hours_m[a] != 0 and hours_m[a] >= week[d]:
                print(a + ': ' + str(week[d]) + ' hour(s)')
                hours_m[a] = hours_m[a] - week[d]
                week[d] = 0
                break
        print()
