text=input()
v="aeiouAEIOU"
co=0

for i in text:
    if i in v:
       
        co+=1

    
print(f"nos are:{co}")


for i in text:
    print(i,end=" ")