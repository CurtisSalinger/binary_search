#!/bin/python3

def find_smallest_positive(xs):
	'''
	Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
	Find the index of the smallest positive number.
	If no such index exists, return `None`.

	HINT: 
	This is essentially the binary search algorithm from class,
	but you're always searching for 0.

	>>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
	4
	>>> find_smallest_positive([1, 2, 3])
	0
	>>> find_smallest_positive([-3, -2, -1]) is None
	True
	'''
	left = 0
	right = len(xs) - 1
	if len(xs) == 0:
		return None
	if xs[right] < 1:
		return None
	if xs[left] > 0 or len(xs) == 1:
		return left
	def go(left,right):
		mid = (right+left)//2
		if right-left == 1:
			return right
		if xs[mid] == 0:
			return mid+1
		if xs[mid] > 0:
			right = mid - 1
		if xs[mid] < 0:
			left = mid + 1
		return go(left ,right)
	return go(left,right)	


def count_repeats(xs, x):
	'''
	Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
	and that x is a number.
	Calculate the number of times that x occurs in xs.

	HINT: 
	Use the following three step procedure:
	1) use binary search to find the lowest index with a value >= x
	2) use binary search to find the lowest index with a value < x
	3) return the difference between step 1 and 2

	I highly recommend creating stand-alone functions for steps 1 and 2
	that you can test independently.

	>>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
	7
	>>> count_repeats([3, 2, 1], 4)
	0
	'''
	if len(xs) == 0:
		return 0
	if len(xs) == 1 and xs[0] == x:
		return 1
	if len(xs) == 1 and xs[0] != x:
		return 0
	if xs[0] == xs[len(xs)-1]:
		return len(xs)
	
	def left_index(xs,x):
		l = 0
		r = len(xs) - 1
		if xs[l] == x:
			print('FIRST ELEM leftmost index = ',l)
			return 0
		def go_left(l,r):
			mid = (l+r)//2
			print('left = ', l,'mid = ', mid , 'right = ',r)
			if r - l <= 1:
				print('leftmost index = ',mid)
				if xs[l] == x:
					return l
				if xs[r] == x:
					return r
				return None
			if xs[mid] > x:
				l = mid
			if xs[mid] <= x:
				r = mid
			return go_left(l,r)
		return go_left(l,r)
	
	
	
	def right_index(xs,x):
		l = 0
		r = len(xs) - 1
		if xs[r] == x:
			print('FIRST ELEM rightmost index = ',r)
			return r
		def go_right(l,r):
			mid = (l+r)//2
			print('left = ',l, 'mid = ', mid , 'right = ',r)
			if r - l <= 1:
				print('rightmost index = ',mid)
				if xs[l] == x:
					return l
				if xs[r] == x:
					return r
				return None
			if xs[mid] >= x:
				l = mid
			if xs[mid] < x:
				r = mid
			return go_right(l,r)
		return go_right(l,r)
	
	
	left = left_index(xs,x)
	right = right_index(xs,x)

	if left == None or right == None:
		return 0
	dif = right - left

	if dif  <= 1 and (xs[left] == x or xs[right] == x):
		#print('\n\n Final left = ', left, 'Final right = ', right, 'Difference = ', dif, 'Final return value = ', 1)
		return 1

	print('\n\n Final left = ', left, 'Final right = ', right, 'Difference = ', dif)
	return (dif + 1)


def argmin(f, lo, hi, epsilon=1e-3):
	'''
	Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
	and that lo and hi are both floats satisfying lo < hi.
	Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

	HINT:
	The basic algorithm is:
		1) The base case is when hi-lo < epsilon
		2) For each recursive call:
			a) select two points m1 and m2 that are between lo and hi
			b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
				depending on which one is the smallest, 
	you recursively call your function on the interval [lo,m2] or [m1,hi]

	>>> argmin(lambda x: (x-5)**2, -20, 20)
	5.000040370009773
	>>> argmin(lambda x: (x-5)**2, -20, 0)
	-0.00016935087808430278
	'''
	'''
	while hi - lo < epsilon:
		m1 = (hi - lo)//3
		m2 = 2*(hi - lo)//3
		if f(lo) <= f(m1):
			hi = m1
		else:
			lo = m1
		if f(m2) >= f(hi):
			lo = m2
		else:
			hi = m2
	return hi
	'''
	print('starts running')
	if abs(hi - lo) < epsilon:
		#print('First if')
		return lo
	
	def go(lo, hi):
		#print('into loop')
		m1 = lo + (hi - lo)/3
		m2 = lo + 2*((hi - lo)/3)
		
		if abs(hi-lo) < epsilon:
		#	print(' F(hi) = ',f(hi), 'F(lo) = ', f(lo))
		#	print('returning FIRST PLACE = ', (hi+lo)/2)
			return (hi+lo)/2
		#print(' M1 = ',m1,' M2 ', m2)
		#print('Low = ', lo,'f(lo) = ',f(lo), 'M1 = ', m1,'f(m1) =',f(m1), 'M2 = ',m2,'f(m2) = ', f(m2),  'High = ',hi,'f(hi) = ',f(hi))
		if f(m2) < f(m1):
			lo = m1
		#	print('\n\nHigh changed to m1\n Low = ',lo,' High = ', hi)
		#else:
		#	lo = m1
		#	print('\n\nLow changed to m1\n Low = ',lo,' M1 = ', m1)
		if f(m2) > f(m1):
			hi = m2
		#	print('\n\nLow changed to m2 \n Low = ',lo,' High = ', hi)
		#else:
		#	hi = m2
		#	print('\n\nHigh changed to m2\n Low = ',lo,' High = ', hi)
		#if abs(f(m2)-f(m1)) < epsilon:
		#	print('returning SECOND PLACE = ', f(lo))
		#	return f(m1)
		#print('Go again')
		return go(lo, hi)
	return go(lo, hi)
