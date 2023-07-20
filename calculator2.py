def add(a, b):
    result = a + b 
    print(int(a) + int(b))
def sub(a, b):
    result = a - b 
    print(int(a) - int(b))
def multiply(a, b):
    result = a * b 
    print(int(a) * int(b))
def div(a, b):
    result = a / b
    print(int(a) / int(b))

while True:
    print("A. Add")
    print("B. Subtract")
    print("C. Multiply")
    print("D. Divide")
    print("E. Exit")
    choice = input("Input your choice: ")

    if choice.lower() == "a":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)
    elif choice.lower() == "b":
        print("Subtract")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub()
    elif choice.lower() == "c":
        print("Multiply")
        a = int(input("Input a fist number: "))
        b = int(input("Input a second number: "))
        multiply()
    elif choice.lower() == "d":
        print("Divide")
        a = int(input("Input a first number: "))
        b = int(input("Input a second number: "))
        div()
    elif choice.lower() == "e":
        print("Program ended")
        quit()
    else:
        print("Invalid choice. Please select a valid option.")
