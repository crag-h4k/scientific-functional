from time import sleep
from sys import maxsize

def fibonacci(n):
	num = [n]
	
	for i in range(maxsize):
		
		y = num[i]+num[i-1]
		b = '{0:b}'.format(y)

		while (len(b)%4) != 0:
			b = '0' + b
		
		num.append(y)
				
		print(b)
		sleep(.1)	
	return fibonacci(n)

fibonacci(1)
