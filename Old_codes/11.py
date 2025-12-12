'''Write a Python program to read a file and find the longest word present in the
file.'''

filename = input("Enter file name: ")
with open(filename, 'r') as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)
