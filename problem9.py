# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import numpy as np
import random
run=True
while run==True:
	a=random.randint(1,332)
	b=random.randint(a+1,499)
	c=1000-a-b
	print "{}+{}+{}={}".format(a,b,c,a+b+c)	
	if a*a+b*b-c*c==0:
		run=False 
		print "{}^2+{}^2-{}^2={}".format(a,b,c,a*a+b*b-c*c)
		print "{}*{}*{}={}".format(a,b,c,a*b*c)
		print "Woah there"
		break
