# 12. Write the program to demonstrate the List collection with all the functionalities.

numbers = [10,20,30,40,50]
print("Original list :" ,numbers)

# Add an element
numbers.append(60)
print("After append:", numbers)

# Add multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)

# Insert at a specific position
numbers.insert(1, 15)
print("After insert:", numbers)

# Update an element
numbers[0] = 5
print("After update:", numbers)

# Remove by value
numbers.remove(15)
print("After remove:", numbers)

# Remove by index
removed = numbers.pop(2)
print("Removed element:", removed)
print("After pop:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Find index
print("Index of 50:", numbers.index(50))

# Search
if 50 in numbers:
    print("50 is present.")

# Count occurrences
numbers.append(50)
print("Count of 50:", numbers.count(50))

# Length
print("Length:", len(numbers))

# Sort
numbers.sort()
print("Ascending:", numbers)

# Reverse
numbers.reverse()
print("Reversed:", numbers)

# Slicing
print("First three:", numbers[:3])
print("Last two:", numbers[-2:])

# Copy
copied_list = numbers.copy()
print("Copied list:", copied_list)

# List comprehension
squares = [n * n for n in numbers]
print("Squares:", squares)

# Clear all elements
numbers.clear()
print("After clear:", numbers)

