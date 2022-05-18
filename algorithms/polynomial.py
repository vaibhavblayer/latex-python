# modeling polynomial - only addition 
class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial{}'.format(self.coeffs)

	def __add__(self, other):
		return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))
