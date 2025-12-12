word=input("Enter the word:")
src=open("sample.txt","r")
dest=open("op.txt","w")

for i in src:          # read line by line
    if word in i:      # check if the word is present in the line
        dest.write(i)  # copy the matching line to op.txt

src.close()
dest.close()

print("Line copied")