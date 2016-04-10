#!/usr/bin/python

import sys

prev_key = -1
print_flag = False
num = -1

for line in sys.stdin:
    curr_key = int(line.strip().split('\t')[0])
    val = line.strip().split('\t')[1]
    if curr_key!=prev_key:
        if prev_key!=-1:
            print_flag = True
            num = cnt
        cnt = 0
    cnt += 1
    if print_flag: #do stuff here
        if prev_key==0:
            print '%d,%d\t%d'%(prev_key,prev_key+4,num)
        elif prev_key==48:
            print '%.2f,infinite\t%d'%(prev_key+.01,num)
        else:
            print '%.2f,%d\t%d'%(prev_key+.01,prev_key+4,num)
        print_flag = False
    prev_key = curr_key

if prev_key==0:
    print '%d,%d\t%d'%(prev_key,prev_key+4,cnt)
elif prev_key==48:
    print '%.2f,infinite\t%d'%(prev_key+.01,cnt)
else:
    print '%.2f,%d\t%d'%(prev_key+.01,prev_key+4,cnt)
