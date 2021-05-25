#  Name - Sarthak Sanjay Sonpatki
# DAY - 3
# AGE CALCULATOR :
# 1)  calculate Age of a person - User should enter the year of birth and the program should output the age..
# eg : entered value is 1990, output age is 30
#
# 2) SIMPLE CALCULATOR:
#  Get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division,
# remainder, power of the input numbers

# AGE CALCULATOR :
print("AGE CALCULATOR")
a = input("Please Enter your Name :- ")
b = int(input("Enter your Birth Year :- "))
c = 2021
print("Welcome ", a)
d = c - b
print("The entered year is {} And your age is {}".format(b,d))

# SIMPLE CALCULATOR:
print("SIMPLE CALCULATOR")
e = int(input("Enter 1st number :- "))
f = int(input("Enter 2nd number :- "))

print("The two numbers are : " , e , "&" , f)
print("The addition is : ", e+f)
print("The subtraction is : ", e-f)
print("The multiplication is : ", e*f)
print("The decimal division is : ", e/f)
print("The floor division is : ", e//f)
print("The remainder is : ", e%f)
print("The exponential is : ", e**f)