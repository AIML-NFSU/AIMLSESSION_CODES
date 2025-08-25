text = "Hello World"
print(len(text))   # Output: 11
print(text.lower())   # hello world
print(text.upper())   # HELLO WORLD
msg = "   welcome   "
print(msg.strip())    # "welcome"
print(text.replace("World", "Python"))  
# Output: Hello Python
words = text.split()  
print(words)   # ['Hello', 'World']


print(text[::-1])
print(''.join(reversed(text)))