# 13. Write the program to demonstrate the Set collection with all the functionalities.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("A:", A)
print("B:", B)

# Add
A.add(10)
print("After add:", A)

# Update
A.update([11, 12])
print("After update:", A)

# Membership
print("3 in A:", 3 in A)

# Remove
A.remove(12)
print("After remove:", A)

# Discard
A.discard(100)
print("After discard:", A)

# Pop
removed = A.pop()
print("Popped element:", removed)
print("A after pop:", A)

# Union
print("Union:", A.union(B))
print("Union using |:", A | B)

# Intersection
print("Intersection:", A.intersection(B))
print("Intersection using &:", A & B)

# Difference
print("A - B:", A - B)
print("B - A:", B - A)

# Symmetric difference
print("Symmetric Difference:", A.symmetric_difference(B))
print("Using ^:", A ^ B)

# Subset and superset
X = {1, 2}
Y = {1, 2, 3}

print("X subset of Y:", X.issubset(Y))
print("Y superset of X:", Y.issuperset(X))

# Copy
copied_set = A.copy()
print("Copied set:", copied_set)

# Set comprehension
even_numbers = {n for n in range(1, 11) if n % 2 == 0}
print("Even numbers:", even_numbers)

# Clear
A.clear()
print("After clear:", A)