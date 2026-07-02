def shutdown():
    """this a function to find when to shutdown your program"""
   
    turnoff = str(input("Do you want to shutdown your program (yes or no)? "))
    update = str(input("Do you want to update your program(yes or no)? "))
    
    if turnoff == "yes" or turnoff == "Yes":
        print("Shutting down your program...")
    elif turnoff == "no" or turnoff == "No":
        print("Aborted shutting down")
    else:
        print("Invalid input")
    

    if update == "yes" or update == "Yes":
        print("Updating your program...")
    elif update == "no" or update == "No":
        print("Aborted updating your laptop")
    else:
        print("Invalid input")
    


print(shutdown())