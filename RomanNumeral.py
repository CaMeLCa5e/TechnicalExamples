"""
3. Write a method that converts its argument from integer to roman numeral """


import re
#Define exceptions 

class roman_error (exception): pass 
class out_of_range_error(roman_error): pass 
class not_integer_error(roman_error): pass
class bad_roman_numeral_error (roman_error): pass

#Define conversion map

roman_numeral_map = (('M', 1000), 
('CM', 900),
('D', 500),
('CD', 400)
('C', 100)
('XC', 90)
('L', 50)
('XL', 40)
('X', 10)
('IX', 9)
('V', 5)
('IV', 4)
('I', 1))

def to_roman(n):
	#convert int to roman numeral 
	if not (0 < n < 4000):
		raise out_of_range_error, 
	if int (n) <> n:
		raise not_integer_error  #can't convert a number that is not an int.
		
	result = ''
	for numeral, integer in roman_numeral_map
		while n >= integer:
			result += numeral 
			n-= integer
	return result
# Define pattern to detect valid roman numerals
roman_numeral_pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?) (IX|IV|V?I?I?I?)$'

def from_roman(s):
	#convert from roman numeral to int
	if not re.search(roman_numeral_pattern, s):
		raise invalid_roman_numeral_error, 'Invalid Roman numeral: %s' % s
		
	result = 0
	index = 0
	
	for numeral, integer in roman_numeral_map:
		while s[index:index+len(numeral)] == numeral:
			result += integer
			index += len(numeral)
	return result
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	