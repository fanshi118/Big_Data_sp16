#!/usr/bin/python

import sys
import StringIO
import csv

for line in sys.stdin:
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        agency = record[-6]
        rev = float(record[14])+float(record[15])+float(record[17])
        print '%s\t%.2f'%(agency, rev)
