# Program 2: Logical operators

x = True
y = False

print("x AND y:", x and y)
print("x OR y:", x or y)
print("NOT x:", not x)


#or

a,b,c=10,45,3

if a>b and a>c:
    print("Greatest is:",a)

elif b>a and b>c:
    print("Greatest is:",b)

else:
    print("Greatest is:",c)