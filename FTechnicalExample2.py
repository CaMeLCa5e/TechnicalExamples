"""
2. Write a method that accepts a list argument and efficiently finds 
and returns a distinct list of any duplicate numbers in the list. 
Include unit tests to verify correct output for a few test lists."""


	
x = [1, 2, 3, 4, 5, 6, 6, 5]

def find_duplicates(lst):
# 	duplicates = []
	

	 return [element for element in set(lst)if lst.count(element) > 1]
# unittest 
assert find_duplicates(x) == [5, 6]





#List Comprehension 
	