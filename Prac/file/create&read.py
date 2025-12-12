#write and read a file

f=open("abc.txt","w")
f.write("Hello how are you")

f.close()
print("Done")

f=open("abc.txt","r")
x=open("c.txt","r")

print(f.read())
print(x.read())
f.close()
