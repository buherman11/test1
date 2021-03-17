#!/usr/bin/env python

import sys
 
if len(sys.argv) != 2:
	raise ValueError('Please provide n.')

n = int(sys.argv[1])

if (n <= 0):
	raise ValueError('n must be > 0.')

if (n > 100):
	raise ValueError('n must be <= 100.')

for h in range(1, n+1):
	s = n - h
	t = ''
	for i in range(0, s):
		t = t + '  '
	for j in range(0, h):
		t = t + ' #'
	print(t)
