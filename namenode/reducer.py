#!/usr/bin/env python
"""reducer.py - Processes key-value pairs received from the mapper.
"""
import sys
from collections import defaultdict

res = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    word, doc = line.split("\t")

    res[word].add(doc)

for word in res:
    docs = sorted(res[word])
    print("{} {}".format(word, ' '.join(docs)))
