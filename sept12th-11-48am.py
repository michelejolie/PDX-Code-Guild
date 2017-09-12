#!/usr/bin/python

# Conditional Statements in Python

var = 100
if var:
  print("A true expression value")
  print(var)

# if and else statement
# the value var is null or zero, So,
# the condition is not satisfied and moved to else statement

var = 0
if var:
# two white spaces, Type the code
    print("A true expression value")
    print(var)
else:
    print("Good bye!")

# while statement

count = 0
while (count < 5):
    print('The count is:', count)
    count = count + 1
print("Good bye!")


# arithmetic progressions using range method with for loop

for var in range(5):
    print(var)