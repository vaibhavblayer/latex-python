# approximating the value of e
import sys

def approxe(n):
		return ( 1.0 + 1.0/n ) ** n

n = int(sys.argv[1])
output = '(1 + 1/{0})**{0} = {1}'.format(n, approxe(n))

print output

