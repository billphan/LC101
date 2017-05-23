# # FUNCTION 1
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

#     if char.isalpha() == False:
#         return char
#     else:
#         newchar = alpha[(alphabet_position(char) + rot) % 26]
#         if char.isupper():
#             return newchar.upper()
#         else:
#             return newchar

from helpers import alphabet_position, rotate_character

# FUNCTION 3 - MODIFIED FOR VIGENERE CIPHER!
# write an encrypt function taking a message and a decryption key
def encrypt(message, key):
    '''This function should implement the vigenere cypher. Should return the message shifted with each character in the key'''

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    idx = 0

    for char in message: # for each character in message
        if char.isalpha():  #if the chracter is alphabetical
            new_char = rotate_character(char, alphabet_position(key[idx])) # calling the rotate_character function taking parameters as nessecary, the alpha pos in relation to key.
            new_message = new_message + new_char # create new message from new_char
            idx = (idx + 1) % len(key) # shift to right divided by length of key
        else:
            new_message = new_message + char
    return new_message

def main():
    '''get a user message and encryption key to rotate'''
    # your main code (input and print statements)

    # BONUS COMMAND LINE ARGUMENTS
    from sys import argv
    print("This is what the user typed on the command line:", argv)

    message = input("Type a message: ")
    print(message)
    key = argv[1]
    # key = input("Encryption key: ")
    # print(key)
    # print new encrypted message
    print(encrypt(message, key))

if __name__ == "__main__":
    main()

# TEST CASE
# message = "The crow flies at midnight!"
# key = "boom"
# expected output = "Uvs osck rmwse bh auebwsih!"
