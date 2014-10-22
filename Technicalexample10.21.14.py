 
"""
2. Write a method that accepts a list argument and efficiently finds 
and returns a distinct list of any duplicate numbers in the list. 
Include unit tests to verify correct output for a few test lists."""

import unittest
class exceptionError (Exception): pass 


#here is the function 
def findDuplicates(list_argument):
	import collections
	return [x for x, y in collections.Counter(list_argument).items() if y>1]

#here is the unittest 
class testTheCharacters(unittest.TestCase):
	def test_no_duplicate_numbers(self):
	
# 	If there are no duplicates in the list, the test should fail
		for s in [2, 3, 5, 5]:
			self.assertEqual(find_duplicates,(s), [5])

			self.assertEqual([5], [5])
		
		
	def areDuplicateNumbers(self):
# 	If there are duplicate numbers in the list, the test should pass
		for s in [2, 3, 4, 5]:
		
			self.assertEqual(find_duplicates ,(s))
	
	
if __name__ == '__main__':
	unittest.main()	
	
	