medical_cause = input("Is there any medical cause? (Yes or no)")

atten = int(input("Attendance of student:"))

if medical_cause == "Yes":
    print("You are allowed")

else: 

    if atten >= 75:
        print("You are allowed")
    
    else:
        print("You are not allowed")

