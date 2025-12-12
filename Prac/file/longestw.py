#find the longest word

f=open("abc.txt","r")
wrd=f.read().split()
print(wrd)

longest=""

for i in wrd:
    if len(i)>len(longest): #here check with the empty str 1st
        longest=i #reassign the value if i to long..
    
print("Longest word:",longest)
print("Len of that words is:",len(longest))