# data-model of polynomial - multiplication

class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial{}'.format(self.coeffs)

	def deg(self):
		return len(self.coeffs)-1

	def __mul__(self, other):
		pol = [0]*(self.deg()+other.deg()+1)
		
		for x in range(len(self.coeffs)):
			for y in range(len(other.coeffs)):
				pol[x+y] += self.coeffs[x] * other.coeffs[y]

		return Polynomial(*(c for c in pol))
