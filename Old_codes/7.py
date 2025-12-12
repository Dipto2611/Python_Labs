'''Write a Python program to create a function is_palindrome(word) that checks
whether a given word is a palindrome or not'''

def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")


