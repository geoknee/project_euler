# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# find sum_of_all_primes_belowo(2000000)
import time
import problem3
import numpy as np
def sum_of_primes_below(x):
    t0=time.clock()
    sum=5
    a=5
    while a < x:
        if problem3.isprime(a):
            sum=sum+a
#            print a
        a=a+2
        if a < x and problem3.isprime(a):
            sum=sum+a
#            print a
        a=a+4
    print "sum={}".format(sum)
    t=time.clock()-t0
    print "{} seconds".format(t)
# TODO THIs is killing me. using various functions
# from problem3.py . how to efficiently get the next
# prime? TRY improving efficiency of prime CHECKING.
# try dividing by 2 then 3 then 5 then 7? cannot 
# allgorithmically produce these though! 
# def sum_of_primes_below(x):
#     bigsum=0
#     f=1
#     for a in range(2,x):
#         bigsum=bigsum+a
#     print "bigsum = {}".format(bigsum)
#     for b in range(2,problem3.largestprimefactor(x)+1):
#         if problem3.isprime(b):
#             print "{} is prime".format(b)
#             c=np.array([0]*int(np.log2(x)/np.log2(b)))
#             for d in range(0,c.size):
#                 c[d]=np.power(b,d+1)
#             print c
#             f=np.kron(c,f)
#             print f
