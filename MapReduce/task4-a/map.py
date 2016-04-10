#!/usr/bin/python

import sys
import csv
import StringIO

for line in sys.stdin:
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        key = record[-10]
        rev = float(record[14])+float(record[15])+float(record[17])
        tip = float(record[17])
        if rev == 0.:
            print key+','+str(rev) +','+str(0.00)
        else:
            print key+','+str(rev)+','+str(tip/rev)
