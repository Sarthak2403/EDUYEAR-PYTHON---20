#  Name - Sarthak Sanjay Sonpatki
# Day-10
# Print following a pattern without using any loop. (Hint use recursive functions)
#
# Examples :
#
# Input: n = 16
# Output: 16, 11, 6, 1, -4, 1, 6, 11, 16
#
# Input: n = 10
# Output: 10, 5, 0, 5, 10


def pattern(n):
    if n<=0:
        print(n)
        return
    else:
        print(n)
        pattern(n-5)
        print(n)
        return

pattern(16)
print()
pattern(10)

