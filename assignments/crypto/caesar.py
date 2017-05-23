# #FUNCTION 1
# # write an alphabet_position function take takes a letter as a parameter
# def alphabet_position(letter):
#     '''This function should find the position 0-26 of the 
#     character in the alphabet and return it's index.'''
    
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     letter = letter.lower()
#     return alpha.find(letter)

# # FUNCTION 2
# # write a rotate_character function, taking a character and a number of rotation
# def rotate_character(char, rot):
#     '''This function should rotate the given character to the right 
#     by the given amount for rotation.'''

#     alpha = "abcdefghijklmnopqrstuvwxyz"

#     # if character is non-alphabetical
#     if char.isalpha() == False:
#         # return characters
#         return char
#     else:
#         # variable newchar assigned to alphabet  
#         newchar = alpha[(alphabet_position(char) + rot) % 26]
#         # if character is uppercase
#         if char.isupper():
#             return newchar.upper() # return uppercase
#         else:
#             return newchar # return new character

from helpers import alphabet_position, rotate_character

# FUNCTION 3
# write an encrypt function taking a message and a decryption key
def encrypt(text, rot):
    '''This function should implement the Caesar cypher.'''
    new_text = ''

    for char in text:
        new_text += rotate_character(char, rot)
    return new_text

def main():
    '''get message and rotation amount to encrypt from user'''
    # your main code (input and print statements)

    # BONUS COMMAND LINE ARGUMENTS
    from sys import argv
    print("This is what the user typed on the command line:", argv)

    message = input("Type a message: ")
    print(message)
    rotation = argv[1]
    # rotation = input(str("Rotate by: "))
    # print(rotation)
    # print new encrypted message
    print(encrypt(message, int(rotation)))

if __name__ == "__main__":
    main()

# TEST CASE
# text = "Hello, World!"
# rotation = 5
# expected output = "Mjqqt, Btwqi!"
