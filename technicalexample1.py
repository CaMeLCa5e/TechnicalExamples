"""Question 1
"""
"""
1. Write a method which will remove any given character from a target string.  
Don't use the String.replace() method in your solution.  
If the given character is not found in the target string, 
your method should raise a CharacterNotFound exception."""

#Define the Exception class
class CharacterNotFound(Exception):
    """Custom CharacterNotFound Exception"""
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
#make an if statement to remove the character, rather than using a string func. 
def remove_character(original_string, character_to_remove):
    found = False
    new_string = ''
    for character in original_string:	
        if character != character_to_remove:
            new_string += character
        else:
            found = True
#return the character to new_string which will be the print statement  
    if found:
        return new_string
    else:
        raise CharacterNotFound(character_to_remove)

if __name__ == '__main__':
    original_string = raw_input('Please enter string: ')
    character_to_remove = raw_input('Character to be removed: ')
    try:
        new_string = remove_character(original_string, character_to_remove)
        print new_string
    except CharacterNotFound as e:
        print "Character not found error:",e
        
        
        
        
        
        
        
        
        
        