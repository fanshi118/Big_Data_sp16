#!/usr/bin/python

import sys

prev_key = ''
prev_med = ''
cnt = 0

for line in sys.stdin:
    l = line.strip().split('\t')
    curr_key = l[0]
    curr_med = l[1]

    if prev_key=='':
        cnt = 1
    elif curr_key!=prev_key:
        print '%s\t%d'%(prev_key,cnt)
        cnt = 1
    else:
        if curr_med!=prev_med:
            cnt += 1 

    prev_med = curr_med
    prev_key = curr_key

print '%s\t%d'%(prev_key,cnt)
