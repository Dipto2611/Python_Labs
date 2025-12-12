'''Write a Python program to print the following numeric pattern:
1
23
456
7 8 9 10'''

num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
