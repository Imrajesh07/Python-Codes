# Program to print all the prime numbers smaller or equal to the given number n
# e.g. Input: 11
# Output: 2 3 5 7 11

from math import sqrt
n = int(input("Enter a positive Integer: "))

for i in range(2, n+1):
    flag = 0
    limit = int(sqrt(i))
    for j in range(2, limit + 1):
        if i == 2:
            print(2, end=' ')
        elif i % j == 0:
            flag = 1
        else:
            pass
    if flag == 0:
        print(i, end=" ")
