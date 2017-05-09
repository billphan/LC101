'''
Chapter 9 - Weekly Graded Assignment
Write a function that mirrors its argument.
For example, mirror('good') should return a string holding the value gooddoog.
'''

# defining and creating a mirror function
def mirror(text):
    # creating a variable 'reverse' assigned to mirrored text, -1 reversing the order printed.
    reverse = text[::-1]
    # returning original text concatenated with reversed string
    return text+reverse
    
# Don't copy these tests into Vocareum
from test import testEqual
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')
