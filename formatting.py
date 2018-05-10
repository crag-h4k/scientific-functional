#integer to string of 0's and 1's

def to_binary(n,length):
	bits = '{0:b}'.format(n)
	while len(bits) != length:
			bits = '0' + bits
	return bits

def print_binary(n,length):
	bits = '{0:b}'.format(n)
	while len(bits) != length:
			bits = '0' + bits
	print(bits)
