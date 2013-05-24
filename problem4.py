#  Find the largest palindrome made from the product of two 3-digit numbers.
for x in range(900,999)[::-1]:
	for y in range(900,999)[::-1]:
		string=str(x*y)
		if string==string[::-1]:
			print "{} times {} equals {}".format(x,y,string) 
