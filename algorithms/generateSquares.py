# Generator for square of numbers

import  sys

def generateSquares(n):
	for i in range(n):
		yield i**2

print(list(generateSquares(int(sys.argv[1]))))

