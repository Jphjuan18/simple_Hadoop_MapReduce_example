#!/usr/bin/env python
import sys

stop_words = ['the', 'does', 'and', 'until', 'thus']

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace & lowercase
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
    	if word not in stop_words:
            print '%s\t%s' % (word, "1")
