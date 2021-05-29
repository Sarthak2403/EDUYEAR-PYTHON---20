#  Name - Sarthak Sanjay Sonpatki
# Day-6
#
# Common part ->  Create a list of n numbers
#
# Q1. Count even numbers and odd numbers
#
# Q2. Tell max and min of the list ( without using any inbuilt function like max(),min())
#
# Q3. Check whether the whole list is palindrome or not( eg. [1,2,1] gives yes for palindrome while [1,2,2] doesn't
#
# Q4. Print the numbers which are palindrome inside the list.

a=[1,2,22,66,44,85,963,764,1000]
#a=[1,2,1]
print(a,"=",len(a))
a_count=0
b_count=0
for i in range(len(a)):
    if a[i]%2==0:
        #print(a[i])
        a_count+=1
    else:
        b_count+=1

print("The even Numbers are :",a_count)
print("The odd Numbers are :",b_count)

c= sorted(a)
print("\nThe Sorted List is :- ",c)
print("The smallest element is ",c[0],"& The largest element is ",c[-1])

b=a[::-1]
print('\nThe reversed list is :- ',b)
if b == a:
    print("The given list is a Palindrome")
else:
    print("The given list is not a Palindrome")

# logic for checking of palindrome inside a string is that
#  to convert the list into a sting
# then to reverse it and check with the original
print("\nChecking of Palindrome inside the List :")
for i in range(len(a)):
    A= a[i]
    Pal=str(A)
    Pal=Pal[::-1]
    Pal=int(Pal)
    if Pal == A:
        print(f"{A} is a Palindrome")
    else:
        print(f"{A} is Not a Palindrome")