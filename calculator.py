def main():
    x = int(input("Enter a number: "))
    print("The square of the number is:", square(x))

def square(x):
    return pow(x, 2)


main()