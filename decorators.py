def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("The function has been executed.")
    return wrapper

@announce
def hello():
    print("Hello, world.")

hello()