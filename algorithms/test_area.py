import  unittest
from area import area
from math import pi


class TestCircleArea(unittest.TestCase):
	def test_area(self):
		self.assertAlmostEqual(area(1), pi)
		self.assertAlmostEqual(area(0), 0)
		self.assertAlmostEqual(area(2.3), pi*2.3**2)

	def test_values(self):
		self.assertRaises(ValueError, area, -2)

	def test_types(self):
		self.assertRaises(TypeError, area, 3 + 2j)
		self.assertRaises(TypeError, area, True)
		self.assertRaises(TypeError, area, 'radius')
