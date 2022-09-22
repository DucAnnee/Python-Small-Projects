from turtle import showturtle
from art import logo 
from os import system

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = int(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    cont = True
    while cont == True:
        operation = input("Choose one operation: ")
        num2 = int(input("What's the next number? "))
        function = operations[operation]
        result = function(num1,num2) 

        print(f'{num1} {operation} {num2} = {result}')
        
        if input(f'Type "y" to continue with {result}, "n" to start a new calculation: ') == 'y':
            num1 = result
            cont = True
        else:
            cont = False
            calculator()

calculator()