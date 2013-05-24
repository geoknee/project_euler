# The aim of the game is to find the sum of all natural numbers <1000 that are multiples of 3 or 5
import time
x=0
a=0
t0=time.clock()
while x < 1000:
	if x%3==0 or x%5==0:
		a=a+x
	x=x+1
print a
t=time.clock() -t0
print "it took %f seconds " % t
 
