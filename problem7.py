# What is the 1001st prime number?
import numpy as np
import time
t0=time.clock()
def isprime(d):
	x=2
	while x <= np.sqrt(d):
		if d%x==0:
			return False
		else:
			x=x+1
	return True
d,e=1,2
while d<=10001:
	if isprime(e):
		print "{} is the {}th  prime".format(e,d)
		d=d+1
	else:
		print e
	e=e+1
t1=time.clock()
print "{} seconds".format(t1-t0)
