#  Name - Sarthak Sanjay Sonpatki
# DAY - 4
# 1) use string functions to count the occurrence of 'y' in a word given by user.
#
# 2) take input of a string and print it's even indexed characters
#
# 3)create a program to swap case. Using string functions
# Input : EdUyEaR
# Output :.  eDuYeAr

# Occurrence of a Character:-
print("Occurrence of a Character:-")
a =input("Enter the String : ")
print(" The occurrence of y in the given string is : " ,a.count('y'))

# Indexed Characters :-
print("Indexed Characters :-" )
b=input("Enter the String : ")
print(" The even indexed characters of the string are : " , b[0 : :2])

# Swapping of Characters :-
print("Swapping of Characters :-")
c=input("Enter the String : ")
print(" The swapped string is : ", c.swapcase())