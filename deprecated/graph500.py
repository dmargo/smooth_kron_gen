#!/usr/bin/python
import sys
from math import exp, log

from scipy.special import binom

def isolated_vertex_count(l, delta = 16., sigma = (0.42 + 0.19) - 0.5):
	l, delta, sigma = int(l), float(delta), float(sigma)
	assert(l % 2 == 0) #TODO: find the complete expression for odd l

	n = 2**l
	m = n * delta

	theta = (1 + 2*sigma) / (1 - 2*sigma)
	gamma = delta*(1 - 4*sigma**2)**(l/2)

	count = sum( (( binom(l, l/2 + r) * exp(-2*gamma*theta**r) \
	                for r in xrange(-l/2, l/2 + 1) )) )
	return count

# Given n and m, returns the best-fit l and d
def parameter_solver(n,m):
	n,m = int(n), int(m)

	# Guaranteed to be positive for the initial value n == 2**l
	loss = lambda l: n - (2**l - isolated_vertex_count(l, float(m) / 2**l))

	# Why bisect when the search is probably ~4 values?
	l = int(log(n,2))
	if l % 2 != 0: l -= 1

	lower = loss(l)
	upper = loss(l + 2)

	while upper > 0:
		l += 2
		lower = upper
		upper = loss(l + 2)
	if abs(upper) > lower: l += 2

	return l, float(m) / 2**l

# Given fixed l and d, returns the best-fit m
def parameter_solver_2(l,d, threshold = 0.1):
    l,d = int(l),float(d)
    n = 2**l

    m = d * n
    vtx = n - isolated_vertex_count(l, d)
    deg = float(m)/vtx

    while deg - d > threshold:
        m = d * vtx
        vtx = isolated_vertex_count(l, float(m)/n)
        deg = float(m)/vtx

    return m


if __name__ == '__main__':
	print(parameter_solver_2(*sys.argv[1:]))
