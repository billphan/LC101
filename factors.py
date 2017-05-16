# create a function factors that takes in an integer n and generates a dictionary that contains the factors of all values from 1 to n.

# creating a dictionary? 
factor = {}
factor['1'] = '1'
factor['2'] = '1,2'
factor['3'] = '1,3'
factor['4'] = '1,2,4'

def factors(n):
  #start with an empty list
  factorList = []
  # for every number in range from 1 to n   
  for i in range(1, n + 1):
    # if n is factorable by a number
    if n % i == 0:
      # append it onto factorList, else not append
      factorList.append(i)
  # return the factored list
  return factorList
# test print factor
print(factors(9))

# Gather our code in a main() function
def main():

# Standard boilerplate to call the main() function to begin the program.
  if __name__ == "__main__":
    main()
