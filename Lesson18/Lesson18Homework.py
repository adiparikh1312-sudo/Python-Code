try:
    age = input("Enter age: ")

    if not age.isdigit():
        raise ValueError

    age = int(age)

    print("Valid age")

    if age % 2 == 0:
        print("Even age")
    else:
        print("Odd age")

except:
    print("Invalid age")

finally:
    print("Program execution complete")