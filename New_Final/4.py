# Program 4: Generate AP series and find its sum

a = 2      # first term
d = 3      # common difference
n = 5      # number of terms

ap = []
for i in range(n):
    ap.append(a + i*d)

print("AP Series:", ap)
print("Sum of AP:", sum(ap))
