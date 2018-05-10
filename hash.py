from time import sleep
from sys import maxsize
from random import randint
from formatting import to_binary, print_binary

def XOR(p):
	q = randint(0,2^64)
	arr  = [p , q]
	print_binary(p,2^64)
	print_binary(q,2^64)

	for i in range(2^10000):
		r = arr[i] ^ arr[i-1]
		arr.append(r)
		print_binary(r,2^64)
		arr[i] = randint(0,2^64)
		sleep(.2)
	
	return r

def OR(p):
	q = randint(0,2^128)
	arr  = [p , q]
	print_binary(p,2^128)
	print_binary(q,2^128)

	for i in range(2^10000):
		r = arr[i] | arr[i-1]
		arr.append(r)
		print_binary(r,2^128)
		arr[i] = randint(0,2^128)
		sleep(.2)
	
	return r


#XOR(randint(0,2^128))

XOR(randint(0,2^128))
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
