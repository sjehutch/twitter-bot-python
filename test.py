#!/usr/bin/env python

with open("test.txt", "w") as file:



 ids=["B3","\nB4","\nB5","\nB6"]

 for i in ids :
      file.write(i)



# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("yo yo yo ")