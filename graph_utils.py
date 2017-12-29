#!/usr/bin/python

def edges(filename):
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line[0] == '#': continue
			src,tar = line.split()
			yield(int(src),int(tar))

def sizeof_graph(filename):
	return 1 + max((max(src,tar) for src,tar in edges(filename)))

import math
def graph_info(filename):
	maxv = 0
	minv = float('inf')
	vertices = set()
	edge_count = 0

	for (src,tar) in edges(filename):
		maxv = max(maxv,src,tar)
		minv = min(minv,src,tar)
		vertices.add(src)
		vertices.add(tar)
		edge_count += 1

	print 'MAX_VERTEX=%d' % maxv
	print 'MIN_VERTEX=%d' % minv
	print 'VERTEX_COUNT=%d' % len(vertices)
	print 'EDGE_COUNT=%d' % edge_count

	s = int(math.floor(math.log(len(vertices), 2)))
	e = int(round(float(edge_count)/(2**s)))
	print
	print 'RMATSMALL_S=%d' % s
	print 'RMATSMALL_E=%d' % e

	s = int(math.ceil(math.log(len(vertices), 2)))
	e = int(round(float(edge_count)/(2**s)))
	print
	print 'RMATBIG_S=%d' % s
	print 'RMATBIG_E=%d' % e

import sys
if __name__ == '__main__':
	graph_info(sys.argv[1])
