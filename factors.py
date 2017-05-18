# create a function factors that takes in an integer n and generates a dictionary that contains the factors of all values from 1 to n.

# creating a function called factors that take n as a parameter
def factors(n):
    # creating a dictionary
    factor_dict = {1: [1]}
    # creating a for loop that takes a range of 2 to n append next integer
    for num in range(2,n+1):
        #start with an empty list
        factor_list = []
        # add onto factor_list
        factor_list.append(1)
        for i in range(2,num):
            # if the number modulo i is even
            if num % i == 0:
                # append it onto list
                factor_list.append(i)
        factor_list.append(num)
        factor_dict[num] = factor_list
    return factor_dict

# Gather our code in a main() function
def main():
    upper_factor_range = input("Enter a number to get the factors of each number up to your number.\n")
    print(factors(int(upper_factor_range)))

# Standard boilerplate to call the main() function to begin the program.
if __name__ == "__main__":
    main()
