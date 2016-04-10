#!/usr/bin/python

import sys

prev_key = ''

for line in sys.stdin:
    a, b = line.strip().split('\t')
    curr_key = a
    if curr_key!=prev_key:
        if prev_key!='':
            print prev_key+'\t',cnt
        else:
            pass
        cnt = 1
    else:
        cnt += 1
    prev_key = a

print prev_key+'\t',cnt
