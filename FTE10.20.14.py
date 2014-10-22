"""
3. Write a method that converts its argument from integer to roman numeral """

"""roman numeral test cases"""


import re
import unittest

#Define exceptions 

class roman_error (Exception): pass 
class out_of_range_error(roman_error): pass 
class not_integer_error(roman_error): pass
class bad_roman_numeral_error (roman_error): pass

#Define conversion map

roman_numeral_map = (('M', 1000), 
						('CM', 900),
						('D', 500),
						('CD', 400),
						('C', 100),
						('XC', 90),
						('L', 50),
						('XL', 40),
						('X', 10),
						('IX', 9),
						('V', 5),
						('IV', 4),
						('I', 1))
	
def to_roman(n):
	#convert int to roman numeral 
	
	if not (0 < n < 4000):
		raise out_of_range_error() 
	if int(n) <> n:
		raise not_integer_error()  
		
	result = ''
	for numeral, integer in roman_numeral_map:
		while n >= integer:
			result += numeral 
			n-= integer
	return result
	
# Define pattern to detect valid roman numerals
roman_numeral_pattern = re.compile ('^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$')

def from_roman(s):
	#convert from roman numeral to int
	if not re.search(roman_numeral_pattern, s):
		raise bad_roman_numeral_error, ('Invalid Roman numeral: %s' % s)
		
	result = 0
	index = 0
	
	for numeral, integer in roman_numeral_map:
		while s[index:index+len(numeral)] == numeral:
			result += integer
			index += len(numeral)
	return result
	

class to_roman_bad_input(unittest.TestCase):
	def test_zero(self):
# 	Program should fail with a 0 input
		self.assertRaises(out_of_range_error, to_roman, 0)
	
	def test_negative(self):
# 	Program should fail if number is negative
		self.assertRaises(out_of_range_error, to_roman, -1)
	
# 	def test_non_int(self):
# # 	Program should fail with a non-integer input
# 		self.assertRaises(ValueError, to_roman, 0.5)
# 	
# class from_roman_bad_input(unittest.TestCase):

# 	def test_too_many_repeated_numerals(self):
# # 	Program should fail with too many repeted numerals
# 		for s in ('MMMM', 'D', 'VV', 'LL', 'XXXX', 'CCCC', 'IIII'):
# 			self.assertRaises(bad_roman_numeral_error, from_roman, s)
			
	def test_repeated_pairs(self):
# 	Application should fail if characters are repeated ie IVIV
		for s in ('CMCM', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
			self.assertRaises(bad_roman_numeral_error, from_roman, s)
			
	def test_incorrectly_formed_numeral(self):
# 	If numeral is incorrectly formed or formed backwards
		for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX'):
			self.assertRaises(bad_roman_numeral_error, from_roman, s)
			
class sanity_check(unittest.TestCase):
	def test_sanity(self):
# 	from_roman(to_roman(n)) == n for all n
		for integer in range(1, 4000):
			numeral = to_roman(integer)
			result = from_roman(numeral)
			self.assertEqual(integer, result)
			
class case_check(unittest.TestCase):
	def test_to_roman_case(self):
# 	roman numerals should always be printed in uppercase
		for integer in range(1, 4000):
			numeral = to_roman(integer)
			self.assertEqual(numeral, numeral.upper())

	def test_from_roman_case(self):
# 	Application should only accept upper case
		for integer in range(1, 4000):
			numeral = to_roman(integer)
			from_roman(numeral.upper())	
			self.assertRaises(bad_roman_numeral_error, from_roman, numeral.lower())
		

if __name__ == '__main__':
	unittest.main()	


