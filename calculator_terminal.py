import math

def add(a, b):
    print(a+b)
def sub(a, b):
    print(a-b)
def multi(a, b):
    print(a*b)
def div(a, b):
    print(b/a)
def mod(a, b):
    print(a%b)
def power(a, b):
    print(a**b)
def sqrt(a):
    print(math.sqrt(a))
def abs(a):
    print(abs(a))
def log(a, b):
    print(math.log(a, b))
def sine(a):
    print(math.sin(a))
def cos(a):
    print(math.cos(a))
def tan(a):
    print(math.tan(a))

while True:
    op = input("Enter the Operationg to be proceeded with: ")
    if op.lower() == "addition":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the first number: "))
        add(a, b)
    elif op.lower() == "substract":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the first number: "))
        sub(a, b)
    elif op.lower() == "multiply":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the first number: "))
        multi(a, b)
    elif op.lower() == "division":
        a = int(input("Enter the denominator: "))
        b = int(input("Enter the numerator: "))
        div(a, b)
    elif op.lower() == "modulo":
        a = int(input("Enter the divident: "))
        b = int(input("Enter the divisor: "))
        mod(a, b)
    elif op.lower() == "exponentiation":
        a = input("Enter the base number: ")
        b = input("Enter the power: ")
        power(a, b)
    elif op.lower() == "square root":
        a = int(input("Enter the number you want to use for the square root: "))
        sqrt(a)
    elif op.lower() == "absolute":
        a = int(input("Enter the absolute value: "))
        abs(a)
    elif op.lower() == "logarithm":
        a = int(input("Enter the number: "))
        b = int(input("Enter the base: "))
        log(a, b)
    elif op.lower() == "sine":
        a = int(input("Enter the angle in radians: "))
        sine(a)
    elif op.lower() == "cosine":
        a = int(input("Enter the angle in radians: "))
        cos(a)
    elif op.lower() == "tangent":
        a = int(input("Enter the angle in radians: "))
        tan(a)
    elif op.lower() == "exit":
        break
    else:
        print("Wrong Input")
