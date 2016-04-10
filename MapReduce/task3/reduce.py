#!/usr/bin/python

import sys

prev_key = ''
t_list = []
l_list = []

for line in sys.stdin:
    curr_key, val = line.strip().split('\t')
    if curr_key!=prev_key:
        if prev_key:
            for t in t_list:
                for l in l_list:
                    print prev_key+'\t'+t+','+l
            t_list = []
            l_list = []

    if 'MEDALLION' not in val: #from table
        t_list.append(val)
    else: #from licenses
        l_list.append(val)
    prev_key = curr_key

for t in t_list:
    for l in l_list:
        print prev_key+'\t'+t+','+l
