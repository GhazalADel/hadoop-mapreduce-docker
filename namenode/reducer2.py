#!/usr/bin/env python
import sys
from collections import defaultdict

res = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    doc, word = line.split("\t")

    res[doc][word] += 1

k = 3

for doc in res:
    top_words = sorted(res[doc].items(), key=lambda x: x[1], reverse=True)[:k]
    
    for word, count in top_words:
        print("%s,%s,%d" % (doc, word, count))
