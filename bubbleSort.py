# Sorts a list using bubble sort.
def bubble_sort(list):
# defining bubble_sort function passing lst as a parameter
""" Sorts a list using bubble sort.
Does not alter the original list but returns a sorted version of it.
"""
    # TODO your code here
    is_sorted = False
    
    # while loop (until condition is met) it is false, no more swaps made
    while is_sorted == False:
        
        # number of swaps made set to 0 to start
        nswaps = 0
        
        # for loop - number in range of length of list
        for num in range(len(list) - 1):
            a = list[num]
            b = list[num + 1]
            
            # if a is greater than b
            if a > b:
                # swap a and b
                list[num] = b
                list[num + 1] = a
                
                nswaps = nswaps + 1
                    
        # if nswaps equals 0    
        if nswaps == 0:
            # set to is_sorted to True
            is_sorted = True
            
    # return final lst
    return list
    
from test import testEqual
testEqual(bubble_sort([0]), [0])  # Sorts a single element, returns same list
testEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
testEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
testEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
