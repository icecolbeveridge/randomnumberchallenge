# simulator

import random

N = 1000
T = 1000
results = {}

def slot1(x,y,z):
	if y < x or z < x:
		return False
	if y < (1+x)/2.:
		return z > y
	else:
		return z < y

def slot2(x,y,z):
	return (y>x and z<x) or (y<x and z>x)

def slot3(x,y,z):
	return slot1(1-x,1-y,1-z)

for i in range(N):
	w1, w2, w3 = 0.,0.,0.
	x = float(i) / (N+1)
	for j in range(T):
		y = random.random()
		z = random.random()
		w1 += slot1(x,y,z) == True
		w2 += slot2(x,y,z) == True
		w3 += slot3(x,y,z) == True
	print(f"{x}\t{w1/T:0.4f}\t{w2/T:0.4f}\t{w3/T:0.4f}")

