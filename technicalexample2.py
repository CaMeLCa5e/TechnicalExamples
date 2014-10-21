 
"""
2. Write a method that accepts a list argument and efficiently finds 
and returns a distinct list of any duplicate numbers in the list. 
Include unit tests to verify correct output for a few test lists."""

import unittest
class exception_error (Exception): pass 


#here is the function 
def find_duplicates(list_argument):
	import collections
	print [x for x, y in collections.Counter(list_argument).items() if y>1]

#here is the unittest 
class test_the_characters(unittest.TestCase):
	def no_duplicate_numbers(self):
	
# 	If there are no duplicates in the list, the test should fail
		for s in [2, 3, 5, 5]:
			self.assertRaises(exception_error, find_duplicates,s)
		
		
	def are_duplicate_numbers(self):
# 	If there are duplicate numbers in the list, the test should pass
		for s in [2, 3, 4, 5]:
			self.assertRaises(true, find_duplicates ,s)
	
	
if __name__ == '__main__':
	unittest.main()	
	
	