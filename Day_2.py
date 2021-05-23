''' Name - Sarthak Sanjay Sonpatki
 DAY - 2
Assignment 1- Create a small program
1. Take variables with values of different types

2. Print these in different lines and with appropriate messages (use .format())

3. Use Real world example of variables. '''

print('DAY 2' , end=" ")
print("Assignment 1" , sep=' ')

# Declarartions of Variables
a = 2021
a1= type(a)
b = 1.38
b1= type(b)
c = "BMW G7"
c1= type(c)
d = True
d1= type(d)

# Print  statements
print("The value of a is {} and its data type is {}" .format(a,a1))
print("The value of b is {} and its data type is {}" .format(b,b1))
print("The value of c is {} and its data type is {}" .format(c,c1))
print("The value of d is {} and its data type is {}" .format(d,d1))

print(end = "\n")                                                      #To leave 1 line
print(f'The new {c} launched in the year {a} costs {b} crore')

print( )                                                               #To leave 1 line

# DATA TYPE CONVERSIONS:-
e = float(a)
f = int(b)
g = bool(c)
h = str(d)
print('DATA TYPE CONVERSIONS:-')
print(e , type(e))
print(f , type(f))
print(g , type(g))
print(h , type(h))
print('Thank \nYou!!')