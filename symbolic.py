import sympy
import sympy.functions.combinatorial.numbers

sympy.init_printing()

ps = {0: 1, 1:1}
xs = {}



sn, sk, sa, sb, t = sympy.symbols("n k a b t")

for n in range(1,21):
	for k in range(n+1):
		# print (n,k)
		sk = k
		sa = k 
		sb = n-k
		if k == 0:
			xs[(sa,sb)] = sympy.Integer(0)
		elif k == n:
			xs[(sa,sb)] = sympy.Integer(1)
		else:
			A = sa * ps[sa-1] * ps[sb]
			B = sb * ps[sb-1] * ps[sa]
			xs[(sa,sb)] = sympy.Float(A/(A+B))

		print(f"({(xs[(sa,sb)])},{n})")
	I = 0
	for k in range(n):
		ll = xs[(k, n-k)]
		ul = xs[(k+1,n-k-1)]
		ncr = sympy.functions.combinatorial.numbers.nC(n-1,k)
		i = t**k *(1-t)**(n-k-1)
		ii = sympy.Integral(ps[k]*ps[n-1-k] * ncr * i, (t,ll,ul))
		# print(ii)
		I += ii.doit()
		# print(ii.doit())
	ps[n] = I
	# print(n,ps[n])

for k, v in ps.items():
	print (f"{k}\t{v}")