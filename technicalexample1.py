"""
1. Write a method which will remove any given character from a target string.  
Don't use the String.replace() method in your solution.  
If the given character is not found in the target string, 
your method should raise a CharacterNotFound exception."""


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




original_string = raw_input('Please enter string: ')
character_to_be_removed = raw_input('Character to be removed:')

def remove_character(original_string, character_to_remove):
    new_string = ''
    for character in original_string:	
        while original_string >= 0:
        	next = raw_input(">")
		if len(next) > 0 and next != character_to_be_removed:
        		new_string += new_string  
         
        else:
	 	 	print 'Error: CharacterNotFound'
	
	print 'New String: %d%%' % original_string.new_string

if __name__ == '__main__':
	remove_character(original_string, character_to_remove)
    
    
    
    
    
    
    
    
    
    
    
    

# 
# 
# 
# original_string = raw_input('Please enter the string: ')
# character_to_be_removed = raw_input ('Character to be removed:')
# 
# 
# def remove(original_string, character_to_be_removed):
# 	new_string = ''
# 	# for character in original_string:
# # 		
# # 		if character != character_to_remove:
# # 			new_string += character
# # 		
# # 		return new_string
# # 		
# 	for character in original_string:
#     if character != character_to_remove:
#         new_string += character
# 	return new_string
# 		
# 		
# 		# elif: 
# # 			character != new_string
# 	
# 			
# 	
# 
# 
# # 
# # try:
# # 	s.translate(None, given_character)
# # 	
# # except CharacterNotFound:
# # 	print 'Error: CharacterNotFound'
# # 	
# # else:
# # 	return s
# 	
# 	