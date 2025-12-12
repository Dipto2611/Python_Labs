'''Write a Python program to read the contents of a text file and display the number of lines, words, and characters in the file.'''

file = open("textme.txt","r")
content = file.read()
print(content)

# no. of chars
charcter=content.replace(" ","")
charcter=charcter.replace("\n","")
print("Num of characters: ",len(charcter))

word = content.split()
print("Num of words: ",len(word))

file.seek(0)
lines = file.readlines()

print("Num of lines: ",len(lines))