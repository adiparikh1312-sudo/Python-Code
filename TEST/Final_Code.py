print("Welcome to the Math Calculator")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    def add(num1 ,num2):
        return num1 + num2
    
    def subtract(num1, num2):
        return num1 - num2
    
    def multiply(num1, num2):
        return num1 * num2
    
    def divide(num1 , num2):
        return num1/num2
    
    print("Addition = ", add(num1, num2)) 
    print("Subtraction = ", subtract(num1, num2))
    print("Multiplication = ", multiply(num1, num2))
    print("Division = ", divide(num1, num2) )

except ValueError:
    print("Please enter a decimal number not any other character")
except ZeroDivisionError:
    print("Please do not enter zero as any of your numbers, because you cannot divide any number by zero.")

print("Thank you for using the Math Calculator")
        