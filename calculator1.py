x = float(input("Give me a number: "))
o = input("Give me an operator:")
y = float(input("Give me another number:"))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
elif o == "**" or "^":
    print(x ** y)
else:
    print("Unknown operator")