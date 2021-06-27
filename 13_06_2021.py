#  Name - Sarthak Sanjay Sonpatki

a=int(input("Enter length of list : "))

l1=[]
l2=[]
L={}
for i in range(a):
    b=int(input("Enter the first list : "))
    l1.append(b)

    c=input("Enter the second list : ")
    l2.append(c)

for i in range(len(l1)):
    L[l1[i]]=l2[i]
print(f"The output Dictionary is: {L}")

print()

a1=input("Enter a string to check : ")
b1=[a1[i] for i in range(len(a1)) if a1[i].isalpha() ]
c1=[a1[i] for i in range(len(a1)) if a1[i].isdigit() ]

print("The number of  alphabets are : ",len(b1))
print("The number of  digits are : ",len(c1))

print()

def longest_word(a2):
    b2 = max(a2.split(), key=len)
    print(f"The Longest Word is {b2} and its length is {len(b2)}")

longest_word(a2=input("Enter a string to find the longest word : "))

print()

t=int(input("Enter the number of Iterations : "))
for i in range(1,t+1):
    for j in range(1,i + 1):
        print(i, end ='')
    print()

print()

def prime(A):
    if A > 1:
        for i in range(2, A):
            if A%i!=0:
                return True
            else:
               return False

a3=int(input("Enter a number : "))

i=10
flag=0
if prime(a3):
    while True:
        if int((a3-(a3%i))/i)==0:
            break
        else:
            if prime(int((a3-(a3%i))/i)):
                flag+=1
        i=i*10
if flag!=0 :
    print(f"{a3} is a Russian Prime Number.")
elif flag==0 and int((a3-(a3%10))/10)==0 and prime(a3):
    print(f"{a3} is a Russian Prime Number.")
else:
    print(f"{a3} is not a Russian Prime Number.")

# Alternative Method:-

# def isprime(n):
#     for i in range(2, n):
#         if n%i==0:
#             return False
#     return True
#
# def slice_str(num):
#     num = str(num)
#     num = num[:len(num)-1]
#     if len(num) == 0:
#         return -1
#     return int(num)
#
# while True:
#     if len(str(a3)) < 1:
#         print('It is a russian prime')
#         break
#     if not isprime(a3):
#         print('It is not a russian prime')
#         break
#     else:
#         num = slice_str(a3)
#         if num == -1:
#             print('It is a russian prime')
#             break