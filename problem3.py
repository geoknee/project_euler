# What is the largest prime factor of 600851475143 ?
# putting a little comment here to test rsync onto hal.oerc.ox.ac.uk
# TODO could create a flag -t which will trigger the procedure to be timed! 
import random
import numpy as np
def isprime(d):
    if d==2:
        return True
    else:
            x=2
	    while x <= int(np.sqrt(d))+1:
		    if d%x==0:
			    return False
		    else:
			    x=x+1
	    return True
	
def largestprimefactor(n):
	answer,x=0,2
	while x<n:
#		a=n/x
		if n%x==0 and  isprime(x):
			answer=x
		x=x+1
	return answer

def primes_below(y):
    for x in range(1,y):
        if isprime(x):
            print x

def nextprime(d):
    if d==2:
        return 3
    else:
            e,x=d+1,2
	    while x <= int(np.sqrt(d))+1:
		    if e%x==0:
			    e=e+x+1
		    else:
			    x=x+1
	    return e

def isprime2(d):
    if d==2:
        return True
    else:
        o=2
        while o <= int(np.sqrt(d))+1:
            if d%o==0:
                return False
            else:
                o=nextprime(o)
        return True

def isprime3(d):
    if d==2:
        return True
    else:
        o=2
        while o <= int(np.sqrt(d))+1:
            if d%o==0:
                return False
            else:
                o=nextprime(o)
        return True


