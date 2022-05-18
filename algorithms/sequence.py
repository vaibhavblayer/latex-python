
import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

i = int(sys.argv[1])
j = int(sys.argv[2])
k = int(sys.argv[3])

print(primes[i:j:k])
