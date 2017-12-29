#!/usr/bin/python
from collections import defaultdict
import sys

if __name__ == '__main__':
	if len(sys.argv) < 3: exit(1)
	filename, edgecount = sys.argv[1], int(sys.argv[2])

	degrfreq = defaultdict(lambda: 0)
	with open(filename) as f:
		for line in f:
			prob = float(line.strip())
			degr = int(round(edgecount * prob))
			degrfreq[degr] += 1

	prev = 0
	for degr,freq in sorted(degrfreq.iteritems()):
		for phony in xrange(prev+1,degr):
			None #print phony,0
		print degr,freq
		prev = degr

