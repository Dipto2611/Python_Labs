#count the nos of upper and lower in a text:

s = input("Enter str: ")
up, low = 0, 0

for ch in s:
    if ch.isupper():
        up += 1
    elif ch.islower():
        low += 1

print("Upper:", up)
print("Lower:", low)
