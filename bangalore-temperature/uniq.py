#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv

with open("sorted.csv") as f, open("uniq.csv", "w") as fo:
    reader = csv.reader(f)
    writer = csv.writer(fo)
    prev = ""
    for row in reader:
        if prev != row[0]:
            prev = row[0]
            writer.writerow(row)


