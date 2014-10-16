"""
1. Write a method which will remove any given character from a target string.  
Don't use the String.replace() method in your solution.  
If the given character is not found in the target string, 
your method should raise a CharacterNotFound exception."""


_______________

given_character = 'X'
string = s

try:
	s.translate(None, given_character)
	
except CharacterNotFound:
	print 'Error: CharacterNotFound'
	
else:
	return s
	
	