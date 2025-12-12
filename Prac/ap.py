#ap series:

a,d,n=1,2,5

ap=[a+i*d for i in range(n)]
print("AP series:",ap)
print("Sum:",sum(ap))


######################

a,d,n=2,4,10
ap=[]
for i in range(n):
    ap.append(a+i*d)
print("AP series:",ap)
print("Sum:",sum(ap))