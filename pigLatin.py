def piglatin(string):
    
    words = str.split(string)
    
    for word in words:
        
        print(word[1:] + word[0] + "ay")

piglatin('python code wins')

