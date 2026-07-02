try:
    num1, num2 = eval(input("Enter 2 numbers, separated by a comma: "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is an error and not defined")

except SyntaxError:
    print("Comma is missing, enter a comma between the 2 numbers like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what.")