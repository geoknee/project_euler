# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
y=20
while y < float('inf'):	
		flag = True
		for x in (20,19,18,17,16,15,14,13,12,11):
				if y%x!=0:
					flag = False
					break
		if flag == True:
			print "{} is dividible by all the numbers from 1 to 20.".format(y)
			break
		y=y+20			

