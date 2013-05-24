# Add all even numbers in the Fibonacci sequence that are < 4,000,000
import time
def fibsumevens(n):
	t,nt,nnt=1,1,1
	nnt,runningtotal,stoplight=0,0,0
	t0=time.clock()
	while stoplight<1:
		print t
		nnt=t+nt	
		if nnt>n:
			stoplight=1
		else: 		
			t=nt
			nt=nnt
			if nnt%2==0:
				runningtotal=runningtotal+nt
	print "running total = %i" % runningtotal
	print "next term = %i" % nt
	print "next next term = %i" % nnt
	t=time.clock() -t0
	print "it took %f seconds " % t
