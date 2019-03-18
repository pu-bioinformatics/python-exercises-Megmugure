#!/bin/python

##Q1; Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console.

###creating a while loop
x=0
while x<6:
  print(x)
  x += 1
print("Q1 done")
##Q2; Repeat the previous problem, but the loop will skip printing x = 5 to the console but will print values of x from 6 to 10.

###creating a while loop using continue statement.
x=0
while x<10:
  x +=1
  if x !=5:
     print(x)

print("Q2 done")
##Q3; Create a for loop that prints values from 4 to 10 to the console.

###creating a for loop.

for i in range(4, 11):
  print(i)

print("Q3 done")
