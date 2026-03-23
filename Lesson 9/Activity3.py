print("What type of vehicle do you want?")
print ("1. Car")
print ("2. Bike")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 2:
    print("What bike do you want?")
    print("\n 1. Scooter")
    print("\n 2. Scooty")
    choice2 = int(input("What type of bike do you want (1 or 2): "))
    
    if choice2 == 1:
        print("You have selected scooter the price of a scooter is ₹56,000")

    elif choice2 == 2:
        print("You have selected scooty the price of a scooty is ₹20,000")

elif choice == 1:
    print("What car do you want?")
    print("1. Sedan")
    print("2. SUV")
    print("3. Both")
    choice3 = int(input("What type of car do you want (1 or 2 or 3): "))

    if choice3 == 1:
        print("You have selected a sedan the cost of a sedan is ₹1,50,00,000")
    
    elif choice3 == 2:
        print("You have selected SUV the cost of an SUV is ₹2,30,00,000")

    elif choice3 == 3:
        print("You have chosen both sedan and SUV, you cannot afford this. \n You should go back home")




