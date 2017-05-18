def get_initials(fullname):
  
  name = (fullname)
  
  full_name = name.split()

  initials = ""

  for name in full_name:
      
    initials += name[0].upper()

  return initials

fullname = input("What's your name? ")

initials = get_initials(fullname)

print("The initials of ", fullname, " are ", initials)
