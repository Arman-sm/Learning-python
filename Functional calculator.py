from os import system
#Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Can't divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def intInputNormalizer(value):
    if value.lstrip("-").isdigit():
        if "-" in value:
            if value.count("-") % 2 == 1:
                value = float(value.lstrip("-")) * -1
            else:
                value = value.lstrip("-")

        value = float(value)

        return int(value) if value.is_integer() else value
    else:
        return "!"

def showOperationsList():
    for item in list(ops.items()):
        print(f"{item[0]}.{item[1][0].capitalize()} ( {item[1][1]} )")

ops = { #Stands for operations
    1 : ["add", "+"],
    2 : ["subtract", "-"],
    3 : ["multiplication", "×"],
    4 : ["division", "÷"],
    5 : ["power", "^"]
}
#Printing the operations list
print("↓ Select operation from the list below ↓")
showOperationsList()
#Programs list
while True:
    operation = input("\nEnter operation index: ")
    
    if operation == 'exit':
        break
    
    if operation == "list":
        showOperationsList()
        continue

    if operation == "clear" or operation == "cls":
        system("cls")
        continue
    
    if operation.isdigit() and int(operation) in ops:
        operation = int(operation)

        num1 = intInputNormalizer(input("First number: "))
        num2 = intInputNormalizer(input("Second number: "))
        if num1 == "!" or num2 == "!":
            print("Invalid Input")
        else:
            print(f"{num1} {ops[operation][1]} {num2} = {globals()[ops[operation][0]](num1, num2)}")
    else:
        print("Invalid Input")