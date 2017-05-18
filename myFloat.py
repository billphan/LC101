def digit_count(float):
    
    my_float = str(float)
    
    for char in range(len(my_float)):
    
        if my_float[char] == '.':
            
            return len(my_float[char + 1:])
        
    return 0

digit_count(3.14)
