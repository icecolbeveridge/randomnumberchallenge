import math

qs = {}
# x is the picked number, k is the lower split, n is how many splits can be made, N is the number of choices

def pk(x,k,n, N):
	pl = (x) / N
	ph = (N-x-1) / N
	return math.comb(n-1,k) * pl**k * ph**(n-k-1) * Q(k, x) * Q(n-k-1, N-x-1)

def Q(n, N):
	if n < 2:
		return 1
	if N == 0:
		return 0
	if (n,N) in qs:
		return qs[(n,N)]
	s = 0.
	for x in range(N):
		p =0
		for k in range(n):
			p_j = pk(x,k,n,N)
			if p_j > p:
				p = p_j
		s += p
	qs[(n,N)] = s/N
	return s/N

for i in range(1,21):
	q = Q(i,1000)
	print( f"({i}, {1/q:.4f})")
