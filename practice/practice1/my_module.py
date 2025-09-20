def add(a, b):
    return a + b

print(f"module1 name is: {__name__}")

if __name__ == "__main__":
    result = add(2, 3)
    print("running directly:", result)
