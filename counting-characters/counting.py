def count_characters(a_string):

    '''my docstring'''

    character_count = {}

    # for every character in a_string
    # the first time I see a character, add it to the set
    # when I see a character again, increment the count

    for character in a_string:

      if character in character_count:

        character_count[character] += 1

      else:
        
        character_count[character] = 1

    return character_count
    
def main():

    """there's your docstring"""

    test_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."""

    print(count_characters(test_string))

if __name__ == "__main__":
  main()
