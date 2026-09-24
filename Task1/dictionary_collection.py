# 14. Write the program to demonstrate the Directory collection with all the functionalities.
student = {
    "name": "Arun",
    "age": 21,
    "mark": 85
}

print("Dictionary:", student)

# Access values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Add a new key-value pair
student["course"] = "Python"
print("After adding course:", student)

# Update a value
student["mark"] = 90
print("After updating mark:", student)

# Update multiple values
student.update({"age": 22, "city": "Chennai"})
print("After update:", student)

# Get keys
print("Keys:", student.keys())

# Get values
print("Values:", student.values())

# Get key-value pairs
print("Items:", student.items())

# Search for a key
if "name" in student:
    print("Name key exists.")

# Remove using pop
removed = student.pop("city")
print("Removed value:", removed)

# Remove the last inserted item
last_item = student.popitem()
print("Removed last item:", last_item)

# Loop through keys
for key in student:
    print("Key:", key)

# Loop through key and value
for key, value in student.items():
    print(key, ":", value)

# Copy
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# Nested dictionary
employees = {
    "E101": {
        "name": "Arun",
        "salary": 50000
    },
    "E102": {
        "name": "Priya",
        "salary": 60000
    }
}

print("Nested dictionary:", employees)

# Access nested value
print("E101 name:", employees["E101"]["name"])

# Dictionary comprehension
squares = {n: n * n for n in range(1, 6)}
print("Dictionary comprehension:", squares)

# Clear
student.clear()
print("After clear:", student)