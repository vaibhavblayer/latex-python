# recursive algorithm for factorial

import sys

def factorial(n):
		if n == 0:
			return 1
		else:
			return n * factorial(n-1)

n = int(sys.argv[1])
output = '{0}! = {1}'.format(n, factorial(n))
print(output)
