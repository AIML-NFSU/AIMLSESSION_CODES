student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}

# Fetching values using keys
print(student["name"])      # Alice
print(student.get("marks")) # 85
student["grade"] = "A"
print(student)
student["city"] = "Kolkata"
print(student)

# Updating values
student["age"] = 21

print(student)
# Removing a key-value pair
del student["course"]

print(student)

student.pop("city")
print(student)


print(student.keys())   # dict_keys(['name', 'course', 'marks', 'grade'])
print(student.values()) # dict_values(['Alice', 'Computer Science', 90, 'A'])

for key, value in student.items():
    print(key, ":", value)
