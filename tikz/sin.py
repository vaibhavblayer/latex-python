# generating table for sin values
import math
import sys

def findSin(n):
		return math.sin(n)

n = int(sys.argv[1])
print '{0:.4f} \t {1:.4f}'.format(math.radians(n), findSin(math.radians(n)))
