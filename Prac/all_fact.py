# Factorial using FOR loop
def fact_for(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Factorial using WHILE loop (DESCENDING)
def fact_while_desc(n):
    fact = 1
    i = n
    while i > 0:
        fact *= i
        i -= 1
    return fact


# Factorial using RECURSION
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n - 1)


# ---- MAIN CODE ----
num = int(input("Enter a number: "))

print("Factorial using for loop:", fact_for(num))
print("Factorial using descending while loop:", fact_while_desc(num))
print("Factorial using recursion:", fact_rec(num))
