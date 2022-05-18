# Algorithm for finding factors
import  sys

def findFactors(n):
	factors = []
	for i in range(1, n//2 + 1, 1):
		if n % i == 0:
			factors.append(i)
	else:
		factors.append(n)
		return factors

n = int(sys.argv[1])
output = '{0} : {1}'.format(n, findFactors(n))

print(output)


