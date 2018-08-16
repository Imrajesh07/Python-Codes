# Program to print the numbers first which has highest frequency of appearance
# e.g. Input: 2,3,2,2,2,3,3,3,4,3,4,4,4,5,4,4,4
# Output: 4,4,4,4,4,4,4,3,3,3,3,3,2,2,2,2,5

numbers = [int(x) for x in input().split(",")]
num_count = {}
count = len(numbers)

for i in numbers:
    if i not in num_count.keys():
        num_count[i] = 1
    else:
        num_count[i] += 1
for key, value in sorted(num_count.items(), reverse=True, key=lambda x: x[1]):
    for j in range(value):
        print(key, end="")
        count -= 1
        if count != 0:
            print(",", end="")
