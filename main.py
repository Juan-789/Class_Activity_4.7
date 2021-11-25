"""
Use  for loops to draw a Christmas tree.. Ask the user how large it should be.
"""
print("How large do u want your christmas tree")
lengthTree = int(input("How large do u want your christmas tree? "))
for i in range (lengthTree,1,-1):
  print (i*"*")
#Creates the descending cascade
for i in range (1, lengthTree+1):
  print(i*"*")
#creates the increasing cascade