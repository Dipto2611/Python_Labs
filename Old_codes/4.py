'''Write a Python program to count how many times each vowel occurs in a given
string.'''

text = input("Enter a string: ").lower()
vowels = "aeiou"
count = {v: text.count(v) for v in vowels}
print("Vowel counts:", count)
