'''Write a Python program to find and display all even numbers from a list of
integers entered by the user.'''

nums = input("Enter numbers separated by space: ").split()
evens = []

for n in nums:
    n = int(n)
    if n % 2 == 0:
        evens.append(n)

print("Even numbers:", evens)
