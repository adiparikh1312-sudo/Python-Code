number1 = 9
square_root = number1 ** 0.5
print("The square root of", number1, "is", square_root)

number2 = 25
square_root2= number2 ** 0.5    
print("The square root of", number2, "is", square_root2)

input_number = int(input("Enter a number to find its square root:"))
input_square_root = input_number ** 0.5
print("The square root of", input_number, "is", input_square_root)

if input_number <= 0:
    print("For a simplified answer please enter a positive number.")
else:
    print("The square root of", input_number, "is", input_square_root)

number3 = 5
square = number3 ** 2
print("The square of", number3, "is", square)

number4 = 7
square2 = number4 ** 2
print("The square of", number4, "is", square2)

input_number2 = int(input("Enter a number to find its square:"))
input_square = input_number2 ** 2
print("The square of", input_number2, "is" , input_square)

print("Please enter your money in multiples of 10:")
money = int(input())

note_00 = money // 100000

note_0 = (money % 1000000)  // 1000

note_1 = ((money % 1000000) % 1000) // 100

note_2 = (((money % 1000000) % 1000) % 100) // 50

note_3 = ((((money % 1000000) % 1000) % 100) % 50) // 10

print("The number of notes of 1000000 is:", note_00)
print("The number of notes of 1000 is:", note_0)
print("The number of notes of 100 is:", note_1)
print("The number of notes of 50 is:", note_2)
print("The number of notes of 10 is:", note_3)