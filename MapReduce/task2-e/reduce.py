#!/usr/bin/python

import sys

prev_day = ''
prev_key = ''
day_count = 0
trip_count = 0

for line in sys.stdin:
    l = line.strip().split('\t')
    curr_key = l[0]
    curr_day = l[1]

    if prev_key == '':
        day_count  = 1 
        trip_count = 1
    elif curr_key != prev_key:
        print '%s\t%d,%.2f'%(prev_key,trip_count,float(trip_count)/day_count)
        day_count  = 1 
        trip_count = 1
    else:
        trip_count += 1
        if curr_day != prev_day:
            day_count += 1

    prev_day = curr_day
    prev_key = curr_key

print '%s\t%d,%.2f'%(prev_key,trip_count,float(trip_count)/day_count)
