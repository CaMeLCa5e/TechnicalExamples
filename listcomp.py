# List comprehension 

x = [1, 2, 3, 4, 5, 6, 6, 5]

def find_duplicates(lst):



# 	duplicates = [] 
# 	for element in set(lst):
# 		if lst.count(element) > 1:
# 			duplicates.append(element)
# 	return duplicates		
     
     
# ####  These are both the same thing written differently. 
     
     
	 return [element for element in set(lst)if lst.count(element) > 1]
	 
	 
	 
	 
	 
# unittest 
assert find_duplicates(x) == [5, 6]

#List Comprehension 