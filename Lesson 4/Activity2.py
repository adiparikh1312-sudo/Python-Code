print("Please enter your amount of money in multiples of 10:")
money = int(input())

note_1 = money // 100

note_2 = (money % 100) // 50

note_3 = ((money % 100) % 50) // 10

print("the number of notes of 100 is:", note_1)
print("the number of notes of 50 is:", note_2)
print("the number of notes of 10 is:", note_3)