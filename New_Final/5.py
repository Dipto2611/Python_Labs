# Program 5: GP Series and its sum

a = 3      # first term
r = 2      # common ratio
n = 5      # number of terms

gp = []
term = a

for i in range(n):
    gp.append(term)
    term *= r

print("GP Series:", gp)
print("Sum of GP:", sum(gp))
