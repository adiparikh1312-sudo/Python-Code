age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("You are allowed to enroll in the class.")
    else:
        print("You are too old to enroll.")
else:
    print("You are too young to enroll.")