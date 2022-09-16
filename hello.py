# Ask a user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalizes only the first character of name
name = name.capitalize()

print("Hello,", name)

# print parameters including sep = ' ' and end = "\n"
# print("Hello, ", name, sep = '', end = "\n");