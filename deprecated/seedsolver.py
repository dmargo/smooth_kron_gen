#!/usr/bin/python
from sympy import Symbol
from sympy.solvers import solve

import sys

if __name__ == '__main__':
	if len(sys.argv) < 2: exit(1)
	skew = float(sys.argv[1])

	a = Symbol('a', positive=True, real=True)
	b = Symbol('b', positive=True, real=True)
	c = Symbol('c', positive=True, real=True)
	eqns = (a+b+c - 1,
	        a/b - skew,
                b/c - skew)
	answ = solve(eqns)
	print(answ)

	a = Symbol('a', positive=True, real=True)
	b = Symbol('b', positive=True, real=True)
	c = Symbol('c', positive=True, real=True)
	d = Symbol('d', positive=True, real=True)
	e = Symbol('e', positive=True, real=True)
	f = Symbol('f', positive=True, real=True)
	eqns = (a+d+f+2*(b+c+e) - 1,
	        a/c - skew,
		c/f - skew,
	        b*b - a*c,
	        d*d - b*e,
	        e*e - c*f)
	answ = solve(eqns)
	print(answ)

	a = Symbol('a', positive=True, real=True)
	b = Symbol('b', positive=True, real=True)
	c = Symbol('c', positive=True, real=True)
	d = Symbol('d', positive=True, real=True)
	e = Symbol('e', positive=True, real=True)
	f = Symbol('f', positive=True, real=True)
	g = Symbol('g', positive=True, real=True)
	h = Symbol('h', positive=True, real=True)
	i = Symbol('i', positive=True, real=True)
	j = Symbol('j', positive=True, real=True)
	k = Symbol('k', positive=True, real=True)
	L = Symbol('L', positive=True, real=True)
	m = Symbol('m', positive=True, real=True)
	n = Symbol('n', positive=True, real=True)
	o = Symbol('o', positive=True, real=True)
	eqns = (a+f+j+m+o+2*(b+c+d+e+g+h+i+k+L+n) - 1,
	        (a*b)/(d*e) - skew, # might be 2 more skew eqns
		(e*i)/(n*o) - skew,
		c*c - a*e,
	        j*j - c*L,
		L*L - e*o,
		b*b - a*c,
		d*d - c*e,
		i*i - e*L,
		n*n - L*o,
		g*g - c*j,
	        k*k - j*L,
	        f*f - b*g,
		m*m - k*n,
		h*h - g*i) # should be equivalently h*h - d*k
	answ = solve(eqns)
	print(answ)
