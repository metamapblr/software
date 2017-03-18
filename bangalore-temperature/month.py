#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv

with open("uniq.csv") as f, open("data.csv", "w") as fo:
    reader = csv.reader(f)
    writer = csv.writer(fo)
    curr_year, curr_month = ["", ""]
    acc = 0
    count = 0
    next(reader, None)
    for row in reader:
        year = row[0][:4]
        month = row[0][4:6]
        day = row[0][6:]
        if curr_year != year or curr_month != month:
            if count != 0:
                writer.writerow([curr_year, curr_month, acc/count])
            acc = 0
            count = 0
            curr_year = year
            curr_month = month
        acc += int(row[1])
        count += 1
        
