f=open("10L.txt","r")

for i in range(10):
    line=f.readline()
    if not line:
        break

    print(line.strip())

f.close()
