#!/usr/bin/python
import numpy as np

from itertools import chain, repeat
import random
import sys

def next_permutation(array, key):
	for i in xrange(len(array)-2,-1,-1):
		if key(array[i]) < key(array[i+1]):
			for j in xrange(len(array)-1,-1,-1):
				if key(array[i]) < key(array[j]):
					array[i],array[j] = array[j],array[i]
					array[i+1:] = reversed(array[i+1:])
					return True
	return False

def unique_permutations(iterable, key):
	p = list(iterable); yield tuple(p)
	while next_permutation(p, key): yield tuple(p)
	raise StopIteration

if __name__ == '__main__':
	if len(sys.argv) < 4: exit(1)
	a,b,s2 = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
	s3 = 0 if len(sys.argv) < 5 else int(sys.argv[4])

	#seed2 = np.array((a,b)); seed2 /= sum(seed2)
	seed2 = np.array((0.75,0.25))

	#seed3 = np.array((a*a,a*b,b*b)); seed3 /= sum(seed3)
	#seed3 = np.array((0.61620459, 0.26759186, 0.11620395))
	#seed3 = np.array((0.523373, 0.302169, 0.174458))
	#seed3 = np.array((0.58415641,  0.28083311,  0.13501048))
        seed3= np.array((.69230769, .23076923, .07692308))

	# Try every unique sequence of seed functions
	sequences = unique_permutations(chain(repeat(seed2,s2),repeat(seed3,s3)), len)
	result = sum( ((reduce(np.kron, seq) for seq in sequences)) ); result /= sum(result)

	for r in result: print(r)



# Old reference implementation, less clear and efficient.
"""
from itertools import imap, permutations
if __name__ == '__main__':
	if len(sys.argv) < 4: exit(1)
	a,b,s2 = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
	s3 = 0 if len(sys.argv) < 5 else int(sys.argv[4])

	c,d,e = a*a, a*b, b*b

	a,b   = a/(a+b),b/(a+b)
	c,d,e = c/(c+d+e), d/(c+d+e), e/(c+d+e)

	seed2 = lambda x: (a*x,b*x)
	seed3 = lambda x: (c*x,d*x,e*x)

	sequences = set(permutations(chain(repeat(True,s2),repeat(False,s3))))

	result = [0.] * 2**s2 * 3**s3
	for seq in sequences:
		distrib = (1.,)
		for use2 in seq:
			f = seed2 if use2 else seed3
			distrib = chain.from_iterable(imap(f, distrib))
		for i in xrange(len(result)):
			result[i] += next(distrib)
		assert next(distrib,None) == None

	norm = sum(result)
	for r in result:
		print(r/norm)
"""
