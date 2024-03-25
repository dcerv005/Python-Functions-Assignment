#Question 1 
#Task 1
def addition(a, b):
    result = a + b
    return result

def subtraction (a,b):
    result = a - b
    return result

def multiplication (a, b):
    result = a * b
    return result

def division (a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:#Task 3
        print("Error: Division by zero is not allowed.")

def modulus (a, b):
    try:
        result = a % b
        return result
    except ZeroDivisionError:#Task 3
        print("Error: Division by zero is not allowed.")

def power (a, b):
    result = a ** b
    return result

def floor_division (a,b):
    try:
        result = a // b
        return result
    except ZeroDivisionError:#Task 3
        print("Error: Division by zero is not allowed.")

while True:
    #Task 2
    a= input("Pick your first number or done: ").upper()
    if a == 'DONE':
        break 
    b = input("Pick your second number or done: ").upper()
    if b == 'DONE':
        break   
    user_input = input("Pick between, [A]ddition, [S]ubtraction, [M]ultiplication, [D]ivision, [MO]dulus, [P]ower, or [F]loor: ").upper()
    if user_input == "A":
        print(addition(int(a), int(b)))
    elif user_input == 'S':
        print(subtraction(int(a), int(b)))
    elif user_input == 'M':
        print(multiplication(int(a), int(b)))
    elif user_input == 'D':
        print(division(int(a), int(b)))
    elif user_input == 'MO':
        print(modulus(int(a), int(b)))
    elif user_input == 'P':
        print(power(int(a), int(b)))
    elif user_input == 'F':
        print(floor_division(int(a), int(b)))
    
    else:
        print('Invalid input')
