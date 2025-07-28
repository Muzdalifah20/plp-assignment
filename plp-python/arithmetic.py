# addition, subtraction, multiplication, or division 
def operation():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation type (+, -, *, or /): ").strip().lower()

    match operation:
        case "+":
            result = num1 + num2 
            return f"{num1} {operation} {num2} = {result}"
        case "-":
            result = num1 - num2 
            return f"{num1} {operation} {num2} = {result}"
        case "*":
            result = num1 * num2 
            return f"{num1} {operation} {num2} = {result}"
        case "/":
                if num1 == 0: 
                     print("Can't divide by Zero!")
                     return None
                else:
                    result = num1 / num2
                    return f"{num1} {operation} {num2} = {result}" 
        case _:
              print("Invalid operation type")

if __name__ == "__main__":
     print(operation())