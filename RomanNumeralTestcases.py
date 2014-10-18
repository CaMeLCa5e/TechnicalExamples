"""roman numeral test cases"""

class to_roman_bad_input(unittest.test_case):
	def test_zero(self):
# 	Program should fail with a 0 input
		self.assertRaises(roman.out_of_range_error, roman.to_roman, 0)
	
	def test_negative(self):
# 	Program should fail if number is negative
		self.assert_raises(roman.out_of_range_error, roman.to_roman, -1)
	
	def test_non_int(self):
# 	Program should fail with a non-integer input
		self.assert_raises(roman.out_of_range_error, roman.to_roman. 0.5)
	
class from_roman_bad_input(unittest.test_case):

	def test_too_many_repeated_numerals(self):
# 	Program should fail with too many repeted numerals
		for s in ('MMMM', 'D', 'VV', 'LL', 'XXXX', 'CCCC', 'IIII'):
			self.assert_raises(roman.bad_roman_numeral_error, roman.from_roman, s)
			
	def test_repeated_pairs(self):
# 	Application should fail if characters are repeated ie IVIV
		for s in ('CMCM', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
			self.assert_raises(roman.bad_roman_numeral_error, roman.from_roman, s)
			
	def test_incorrectly_formed_numeral(self):
# 	If numeral is incorrectly formed or formed backwards
		for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX'):
			self.assert_raises(roman.bad_roman_numeral_error, roman.from_roman, s)
			
class sanity_check(unittest.test_case):
	def test_sanity(self):
# 	from_roman(to_roman(n)) == n for all n
		for integer in range(1, 4000):
			numeral = roman.to_roman(integer)
			result = roman.from_roman(numeral)
			self.assert_equal(integer, result)
			
class case_check(unittest.test_case):
	def test_to_roman_case(self):
# 	roman numerals should always be printed in uppercase
		for integer in range(1, 4000):
			numeral = roman.to_roman(integer)
			self.assert_equal(numeral, numeral.upper())

	def test_from_roman_case(self):
# 	Application should only accept upper case
	for integer in range(1, 4000):
		numeral = roman.to_roman(integer)
		roman.from_roman(numeral.upper())	
		self.assert_raises(roman.bad_roman_numeral_error, roman.from_roman, numeral.lower())
		
if __name__ == '__main__':
	unittest.main()	
		
		
		
		
		