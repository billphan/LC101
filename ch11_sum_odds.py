# Write a function that will sum up all the elements in a list up to but not including the first even number.

def sum_of_initial_odds(nums):
    # your code here
    #set starting sum to 0
    sum = 0
    # for loop to test if element is an odd number - if it's odd, add it to the previous integer
    for i in nums:
        if i % 2 != 0:
            sum = sum + i
    #test if element is an even number - if it's even, don't include it and break code
        else: 
            break
    #return the sum of integers
    return sum
