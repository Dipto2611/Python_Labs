#while loop desc:
n=int(input("Input:"))

fact=1
i=n

while i>0:
    fact*=i
    i=i-1
    
print(fact)

#using for loop:
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial:", fact)
