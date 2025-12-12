#count of lines,char and wrds

f=open("sample.txt","r")

#for reading a file
text=f.read()
print(text)


# for char:

char=text.replace(" ","") #spacing to null
char=char.replace("\n","") #new line to null [must update the text to char] 
# print(char) 
print("count of char:",len(char))

# for words:

wrd=text.split() #will splits in list of char of words
# print(wrd)
print("count of wrds:",len(wrd))

# for line:

# first put the cursor in 1st place then use readlines() then print the len
f.seek(0)
lines=f.readlines()
print("count lines:",len(lines))