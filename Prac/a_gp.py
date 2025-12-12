#ap series:

a,r,n=1,2,5

gp=[ a*(r**i)for i in range(n)]
print("GP series:",gp)
print("Sum:",sum(gp))


######################

a,r,n=2,3,8
gp=[]
for i in range(n):
    gp.append( a*(r**i))
print("GP series:",gp)
print("Sum:",sum(gp))