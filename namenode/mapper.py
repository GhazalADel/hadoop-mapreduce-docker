#!/usr/bin/env python
"""mapper.py - This mapper script reads text input from standard input.
"""
import sys

for line in sys.stdin:
    line = line.strip() 
    doc, text = line.split(",", 1) 
    words = text.split()

    for word in words:
        print("%s\t%s" % (word, doc))
