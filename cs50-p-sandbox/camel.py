def main():
    user_input = input("camelCase: ")
    b = user_input.lower()
    c = list(b)
    str1 = ""
    for x in range(len(c)):
        if ord(user_input[x]) >= 65 and ord(user_input[x]) <= 90:
            c.insert(x, "_")
            x = x + 1
    "".join(c)
    for ele in c:
        str1 += ele
    print("snake_case:", str1)

if __name__ == "__main__":
    main()