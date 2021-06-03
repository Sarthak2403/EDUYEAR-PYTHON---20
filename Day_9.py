#  Name - Sarthak Sanjay Sonpatki
# Day-9
# 1. Take a number from user and check whether it is prime or not. Use parameters to send the number to function.
#
# Eg. Enter a number 3
#        3 is prime
#
# 2. Write a function to print n factorial. Take n value as user input and pass as a parameter
# Eg. Enter a number 5 :
# 120

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num%i!=0:
                print("The given Number is a prime number")
                break
            else:
                print("The given Number is not a prime number")
                break

a=int(input("Enter a number : "))
prime(a)


def factorial(h):
    I = 1
    for i in range(1, h + 1):
        if h < 0:
            print("The Factorial does not exists.")
        elif h == 0:
            print("The factorial of 0 is 1.")
        I = I * i
    print("The factorial of {} is ".format(h), I)

h=int(input("Enter a number : "))
factorial(h)