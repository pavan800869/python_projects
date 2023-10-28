#To make simple calculator

# + - * / % // **


def calculator():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    operation = input("Enter the operation to perform: ")

    
    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)

    elif operation == '/':
        print(float(num1/num2))
    elif operation == '%':
        print(num1%num2)
    elif operation == '//':
        print(num1//num2)
    elif operation == '**':
        print(num1**num2)
calculator()
while(True):
    again = input("Enter [y/n] to calculate again: ")
    if again.lower()!= 'n':
        calculator()
    else:
        break
