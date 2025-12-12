#how to positon the grphs
import matplotlib.pyplot as plt


# -------------------------------
# Subplot 1 (Position 1)
# -------------------------------
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Line Plot - 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# -------------------------------
# Subplot 2 (Position 2)
# -------------------------------
plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C"], [5, 2, 7])
plt.title("Bar Graph - 1")
plt.xlabel("Category")
plt.ylabel("Value")

# -------------------------------
# Subplot 3 (Position 3)
# -------------------------------
plt.subplot(2, 2, 3)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Line Plot - 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# -------------------------------
# Subplot 4 (Position 4)
# -------------------------------
plt.subplot(2, 2, 4)
plt.bar(["A", "B", "C"], [5, 2, 7])
plt.title("Bar Graph - 2")
plt.xlabel("Category")
plt.ylabel("Value")

# Adjust spacing
plt.tight_layout()
plt.show()
