#write a function to reverse a string


# def function(x):
#      return x[::-1]
#
#
# x = input("Enter a string of text here: ")
#
# d = function(x)
#
# print(d)



#write a function to do (get user input) addition function type 1 2 parameters addition result should be sent to subtraction
# subtraction, multiplication and division
#4 functions 2 parameters, all functions should send values to next function in the result of the other

def add(a, b):
     c = a+b
     return c

def sub(a, b):
     c = a - b
     return c

def multi(a, b):
     c = a*b
     return c

def divi(a, b):
     c = a//b
     return c

d = add(10, 20)
e = sub(d, 50)
f = multi(e, 70)
g = divi(f, 40)

print(d, e, f, g)
