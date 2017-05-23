# HELPER DOC

# FUNCTION 1
# write an alphabet_position function take takes a letter as a parameter
def alphabet_position(letter):
    '''This function should find the position 0-26 of the 
    character in the alphabet and return it's index.'''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    return alpha.find(letter)

# TEST CASE
# letter = "Z"
# expected output = 25

# FUNCTION 2
# write a rotate_character function, taking a character and a number of rotation
def rotate_character(char, rot):
    '''This function should rotate the given character to the right 
    by the given amount for rotation.'''
    alpha = "abcdefghijklmnopqrstuvwxyz"

    if char.isalpha() == False: #if character is not alphabetical
        return char
    else:
        newchar = alpha[(alphabet_position(char) + rot) % 26]
        if char.isupper():
            return newchar.upper()
        else:
            return newchar

# TEST CASE
# character = "z"
# rotation = 37
# expected output = "k"
