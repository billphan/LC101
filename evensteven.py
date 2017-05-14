#  ---------------------- Even Steven -------------------------

# INSTRUCTIONS
#
# For each number between 1 and 100...
#   If the number is odd, then simply print it out.
#   BUT if the number is even, then print the word "Steven" instead.

# When I run your program, I should see the following output:
#
#   1
#   Steven
#   3
#   Steven
# 5
#
#   ...
#
# 97
# Steven
# 99
# Steven

# Note that you shold start at 1 (not 0), and that the 100 must be INCLUDED.
# In other words, the last number should be 100, not 99.

# --------------------------------------------------------------------

# Put your Python code here:

# print(range(100+1))

for i in range(1,100+1):
  if i % 2 == 0:
    print("Steven")

  else:
    print(i)















# Classic Interview Problem The problem is famously used in job interviews. See if you can figure it out! Loop through the numbers between 1 and 20. If a number is divisible by 3, print Hip. If the number is divisible by 7, print “Hooray”.

for i in range(1,20,3):
  print("Hip"),
else: 
  print("hooray")
