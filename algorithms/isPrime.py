# Algorithm for checking prime number

import sys

def isPrime(n):
	for i in range(2, n/2 + 1, 1):
		if n % i == 0:
			return False
	else:
		return True

n = int(sys.argv[1])
output = '{0} : {1}'.format(n, isPrime(n))

print output

