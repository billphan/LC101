def get_initials(fullname):
  """ Given a person's name, returns the person's initials (uppercase) """
  # TODO your code here
  # Assign name variable to parameter from function
  name = (fullname)
  # Assign full name to original name split
  full_name = name.split()
  # Assign initials to empty string
  initials = ""
  # Create for loop to check name
  for name in full_name:
    # For every first letter in passed name, uppercase  
    initials += name[0].upper()
  # Return the initials in caps  
  return initials

def main():
    # input asking for user name
    fullname = input(str("What's your name? "))
    # assign initials to user's given name
    initials = get_initials(fullname)
    # print final statement
    print("The initials of " + "'" + fullname + "' are ", initials)
    
if __name__ == '__main__':
    main()
