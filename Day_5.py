#  Name - Sarthak Sanjay Sonpatki
# DAY - 4
# 1. From range n to m, print all the numbers divisible by 5 and 7 both

# 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Given:
# number_of_terms = 5
# So series will become 2 + 22 + 222 + 2222 + 22222
# Expected output:
# 24690
# Hint: 'a'*2 = 'aa'

# Assignment for While Loops
# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print the sum of all numbers. (Use while loop)

# 4.  Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output: 120

# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

print("DIVISIBLE NUMBERS :-" )
for i in range(0 , 100) :
    if i % 5 == 0 :
        print("The Numbers Divisible by 5 are :-",i)
print()
for j in range(0,100):
    if j % 7 == 0:
        print("The Numbers Divisible by 7 are :-", j)

print("\nSUM OF A SERIES:-")
t=int(input("Enter the number of Iterations : "))
s=0
for i in range(1,t+1):
    a='2'*i
    print(a,end='\n')
    s=s+int(a)
print("+")
print("---------------")
print(s)


print()
print("WHILE LOOP:-")
#d=int(input("Enter number :- "))
f=0
g=''
while g != 'q':
    #for i in range(d):
        e=int(input("Enter : "))
        g =input("Fiinish ? : ")
        f=f+e
        if g=='q':
            break
print("The Sum of the Digits is  : ",f)

print("\nFACTORIAL OF A NUMBER:-")
h=int(input("Enter the number whose factorial you want : "))
I=1
for i in range(1, h+1):
    if h<0:
        print("The Factorial does not exists.")
    elif h==0:
        print("The factorial of 0 is 1.")
    I=I*i
print("The factorial of {} is ".format(h), I)

print("\nSTRING MANIPULATION:- ")
str = 'python is a good programming language'
for i in range(len(str)):
    endval="-"

    if str[i]==" ":
        endval=""
    if i == len(str)-1:
        endval=""
    elif str[i+1]==' ':
        endval=""

    if i%2==0:
        print(str[i].upper(),end=endval)
    else:
        print(str[i].lower(),end=endval)

    #print(str[i], end=endval)
