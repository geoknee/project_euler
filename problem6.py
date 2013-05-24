# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
a,b=0,0
for x in range(1,101):
		a=a+(x*x)
		b=b+x
print "the sum of squares is {}, the square of sums is {}, the difference is {}".format(a,b*b,a-b*b)



