# TODO 
# define a function called sum_evens, which receives one argument, a list of numbers.
# your function should return the sum of all the even numbers in the list

# creating a function passing list as a parameter
def sum_evens(list):
    
    #starting count 0
    sum = 0
    
    # creating a for loop taking each number in a list...
    for num in list:
        
        # if the number is divisible by two..
        if(num % 2 == 0):
            
            # than add that number into sum
            sum += num
            
    return sum
