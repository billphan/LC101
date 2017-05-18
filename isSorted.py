def is_sorted(string):

    for index in range(len(string)-1):
        
        if string[index] > string[index + 1]:
            
            return False
        
    return True

is_sorted("Hello")
