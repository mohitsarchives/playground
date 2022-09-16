# Ask a user for their name
from unicodedata import name


def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("Hello,", name)

main()

# Remove whitespace from str
#name = name.strip().title()

# Capitalizes only the first character of name
# name = name.capitalize()

# Capitalizes first character of each word
# name = name.title()

# Split user's name
# first, last = name.split(" ")

# print("Hello,", first)

# print parameters including sep = ' ' and end = "\n"
# print("Hello, ", name, sep = '', end = "\n");