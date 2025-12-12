txt=input("Enter input:")

vowels="aeiouAEIOU"

cnt=0

for i in txt: #1st go into the text part for the searching then go the next  part
    if i in vowels: #then check in the vowels
        cnt+=1

print(f"Nos of vowels are:{cnt}")