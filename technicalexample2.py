"""
2. Write a method that accepts a list argument and efficiently finds 
and returns a distinct list of any duplicate numbers in the list. 
Include unit tests to verify correct output for a few test lists."""


#test list
list_argument = [7, 6, 4, 4, 7, 12, 98] 

def findDuplicates(list_argument):
	import collections
	print [x for x,y in collections.Counter(list_argument).items() if y>1]





