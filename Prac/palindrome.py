#using funcs:

def palin(s):
    return s==s[::-1]

txt=input("Enter string:")

if palin(txt):
    print("Its a palindrome")
else:
    print("Not a palindrome")


#using normal way:

t=input("Enter the text to check:")

if t==t[::-1]:
    print("yes")
else:
    print("no")

