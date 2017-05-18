'''
Write a function analyze_text that receives a string as input.
Your function should count the number of alphabetic characters
(a through z, or A through Z) in the text and also keep track of
how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text, something like this:

The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.

You will need to make use of the isalpha function.
'''

def analyze_text(text):
    # find length of string checking for lowercase and is a letter
    string = [e.lower() for e in text if e.isalpha()]
    # find number of 'e' in string
    count = string.count('e')
    # calculate percentage of 'e' in string
    # percentage = (100.0*count/len(string))
    # assign new result to variable and return it
    result = "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(len(string), count, str(100.0*count/len(string)))
    return result
    
