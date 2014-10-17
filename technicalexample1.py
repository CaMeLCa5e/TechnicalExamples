"""
1. Write a method which will remove any given character from a target string.  
Don't use the String.replace() method in your solution.  
If the given character is not found in the target string, 
your method should raise a CharacterNotFound exception."""

# 
# _____________
# 
# - For #1,  write a for loop instead of
# using any kind of built-in string function. To illustrate:
# 
# def remove(original_string, character_to_remove):
#     new_string = ''
#     for character in original_string:
#         if character != character_to_remove:
#             # add character to new_string here
#         # otherwise ignore the character
#     # return new_string after removing all instances of character_to_remove
# 
# __
# 
# 


original_string = raw_input('Plese enter the string: ')
character_to_be_removed = raw_input ('Character to be removed:')


def remove(original_string, character_to_be_removed):
	new_string = ''
	for character in original_string:
		
		if character != character_to_remove
# 			character += new_string
			
	return new_string
		

 		
		




# 
# try:
# 	s.translate(None, given_character)
# 	
# except CharacterNotFound:
# 	print 'Error: CharacterNotFound'
# 	
# else:
# 	return s
	
	