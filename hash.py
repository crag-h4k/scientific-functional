from time import sleep
from sys import maxsize
from random import randint

def to_binary(n):
	b = '{0:b}'.format(n)
	while (len(b)%4) != 0:
			b = '0' + b	
	print(b)
	return b

def xor(p):
	q = randint(0,maxsize)
	arr  = [p , q]
	to_binary(p)
	to_binary(q)

	for i in range(maxsize):
		y = arr[i] ^ arr[i-1]
		arr.append(y)
		to_binary(y)
		print('\n')
		sleep(.2)

	return xor(p,q)

xor(255)

'''
	for i in range(maxsize):
		
		y = num[i]+num[i-1]
		b = '{0:b}'.format(y)

		while (len(b)%4) != 0:
			b = '0' + b
		
		num.append(y)
				
		print(b)
		sleep(.1)	
		'''
