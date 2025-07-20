num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")

result = 0
match operation: 
    case "+":
        result = num1 + num2
        
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        print("divisible by 0 is not possible")
    case _:
        print("invalid operation")   
    
print("The result is", result, ".")