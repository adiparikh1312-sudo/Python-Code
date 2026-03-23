age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("You are allowed to enroll in the junior class of 10.")
    else:
        print("You are too old to enroll in class of 10.")
else:
    print("You are too young to enroll in all classes.")

#Extension: 
#Class 11 teacher reguires students from age group 21 - 30

if age >= 21:
    if age <= 30:
        print("You are allowed to enroll in the seniors class 11.")
    else:
        print("You are too old to enroll in senior class of 11.")

else:
    print("You are too young to enroll in the senior class of 11.")

#Further Extension:
#Class 12 teacher requires students from age group 31 - 40

if age >= 31:
    if age <= 40:
        print("You are allowed to enroll in highest class of 12.") 
    else:
        print("You are too old to enroll in all classes.")
else:
    print("You are too young to enroll in the highest class of 12")