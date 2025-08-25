fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[1:4])   # ['banana', 'cherry', 'mango']
print(fruits[:3])    # ['apple', 'banana', 'cherry']
print(fruits[2:])    # ['cherry', 'mango', 'orange']
print(fruits[-2:])   # ['mango', 'orange']

print(len(fruits))   # 5
fruits.append("grape")
print(fruits)   # ['apple', 'banana', 'cherry', 'mango', 'orange', 'grape']
fruits.insert(2, "kiwi")
print(fruits)   # ['apple', 'banana', 'kiwi', 'cherry', 'mango', 'orange', 'grape']
fruits.remove("banana")
print(fruits)   # ['apple', 'kiwi', 'cherry', 'mango', 'orange', 'grape']
fruits.pop()      # removes last
print(fruits)

fruits.pop(2)     # removes item at index 2
print(fruits)
