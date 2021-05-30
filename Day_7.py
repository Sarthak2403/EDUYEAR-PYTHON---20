#  Name - Sarthak Sanjay Sonpatki
# Day-7
# 1. Give all the index values of vowels.
# Eg. "abed"
# >> 0 2
#
# 2. Reverse the words of a string
# Input... hello world happy birthday
# Output... birthday happy world hello
#
# 3. Remove duplicate elemnts without using set()
# Ex.
# [1,2,3,3,2,4]
# >> [1,2,3,4]

print("Index Values of Vowels :-")
names=input("Enter a string : ")
print(names , type(names))
names=names.lower()
b = ['a','e','i','o','u']
c=[i for i in range(len(names)) for j in b if names[i]==j]
print("The indexes of Vowels are : ",c)

# ALTERNATIVE METHOD
# for i in range(len(names)):
#     if names[i]=='a':
#         print(f"{names[i]} is a vowel and it is at position {i}")
#     elif names[i]=='e':
#         print(f"{names[i]} is a vowel and it is at position {i}")
#     elif names[i]=='i':
#         print(f"{names[i]} is a vowel and it is at position {i}")
#     elif names[i]=='o':
#         print(f"{names[i]} is a vowel and it is at position {i}")
#     elif names[i]=='u':
#         print(f"{names[i]} is a vowel and it is at position {i}")
#     else:
#         print(f"{names[i]} is not a vowel")

# UNFILTERED WAY OF LIST COMPREHENSIONS
# name=[]
# n = [ i for i in range(len(names)) if names[i]=='a']
# m=[ i for i in range(len(names)) if names[i]=='e']
# m1=[ i for i in range(len(names)) if names[i]=='i']
# e=[ i for i in range(len(names)) if names[i]=='o']
# e1=[ i for i in range(len(names)) if names[i]=='u']
#
# name.append(n)
# name.append(m)
# name.append(m1)
# name.append(e)
# name.append(e1)
#
# print(name)

v = "\nhello world happy birthday"
print(v)
v1=''
s=v.split()
s=s[: :-1]
for i in s:
    v1 += i +' '
print(v1)

print("\nChecking of Duplicate Elements :-")
l=[]
abc=int(input("Enter size = "))
for i in range(abc):
    ab = int(input("Enter the numbers: "))
    l.append(ab)
print(l)
li=[]
for i in l:
    if i not in li:
        li.append(i)
print(li)