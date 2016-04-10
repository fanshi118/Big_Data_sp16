#!/usr/bin/python

import sys

prev_key = ''
f_list = []
t_list = []

for line in sys.stdin:
    if not line.startswith('medallion,hack_license,vendor_id,pickup_datetime'):
        curr_key, val = line.strip().split('\t')
        if curr_key!=prev_key:
            if prev_key: #do stuff here
                for t in t_list:
                    for f in f_list:
                        print prev_key+'\t'+t+','+f
                t_list = []
                f_list = []
        if val.startswith('t'):
            t_list.append(val[1:])
        elif val.startswith('f'):
            f_list.append(val[1:])
	prev_key = curr_key
for t in t_list:
    for f in f_list:
        print prev_key+'\t'+t+','+f
