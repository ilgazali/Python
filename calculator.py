

def convertNum(number): #It is defined to convert the input to float and check for value errors.
     try:
         return float(number)
     except ValueError:
         print('invalid number')

def mathematical_operations(number1, operation, number2): #I have defined a separate function for mathematical operations.

    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '/':
        try:
            return number1 / number2
        except ZeroDivisionError as e: #We caught the error with the try-except structure so that the program does not stop working when the number is divided by 0.
            print("Value cannot be divided by zero")
    elif operation == '*':
        return  number1 * number2
    elif operation == '%':
        return  number1 % number2
    elif operation == '^':
          result = 1
          for s in range(int(number2)):
              result = result * number1
          return result
    else:
       return None


def calculator():
    operators = ["+","-","/","*","%","^"]
    firstNum = None
    operator = None
    secondNum = None
    input_user = "start" #To enter the loop at the beginning, the 'start' string is given and it enters to loop.
    while (input_user != "exit" and input_user != ""):
        input_user = input()
        if input_user == "exit" or input_user == "":
            break
        elif input_user == "clear":
            firstNum = None
            operator = None
            secondNum = None
        elif firstNum is None:
            firstNum = convertNum(input_user)
        elif operator is None:
            if input_user in operators:
                operator = input_user
            else: #if the input_user is a number, the input is reassigned to firsNum.
                firstNum = convertNum(input_user)
        else:
            secondNum = convertNum(input_user)
            print(f'{firstNum} {operator} {secondNum} = {mathematical_operations(firstNum,operator,secondNum)}')
            firstNum = secondNum = operator = None

calculator()