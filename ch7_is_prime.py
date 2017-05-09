'''
Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime number and False otherwise.

As a refresher, a number is prime if it is not divisible by any other number (other than itself and 1).

Also remember that you can use the modulo operator (%) to check whether one number is divisible by another.

Notice that 2, 3, 4, and 6, all the factors of 12, yield 0. This makes sense because modulo returns the remainder after division, and these numbers divide 12 perfectly, so there is no remainder left over.

Anyway, 12 is definitely not prime since it is divisible by a bunch of numbers: 2, 3, 4, and 6.
'''

# TODO 
# define a function is_prime, that takes a single integer argument 
# and returns True when the argument is a prime number and False otherwise

def is_prime(num):  
    
    if num == 1:  
        return False  
    
    elif num == 2:  
        return True;  
     
    else:  
        for x in range(2, num):  
            if num % x == 0:  
                return False
         
        return True
