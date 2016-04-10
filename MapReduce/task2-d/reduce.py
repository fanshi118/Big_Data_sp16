#!/usr/bin/python

import sys

prev_key = ''

for line in sys.stdin:
    curr_key, val = line.strip().split('\t')
    val1 = float(val.strip().split(',')[0])
    val2 = float(val.strip().split(',')[1])
    if curr_key!=prev_key:
        if prev_key!='':
            print '%s\t%.2f,%.2f'%(prev_key,rev,toll)
        rev = 0
        toll = 0
    rev += val1
    toll += val2

    prev_key = curr_key

print '%s\t%.2f,%.2f'%(prev_key,rev,toll)
