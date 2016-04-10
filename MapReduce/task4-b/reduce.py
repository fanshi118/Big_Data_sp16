#!/usr/bin/python

import sys

prev_key = ''
cnt = 0
k = 20
d = {}

for line in sys.stdin:
    curr_key = line.strip().split('\t')[0]
    val = float(line.strip().split('\t')[1])
    if curr_key!=prev_key:
        if (prev_key!=''):
            d[prev_key] = rev
        rev = 0
    rev += val
    prev_key = curr_key
d[prev_key] = rev

for key, val in sorted(d.items(), key=lambda x: x[1], reverse=True):
    if cnt==k:
        break
    cnt += 1
    print '%s\t%.2f'%(key,val)
