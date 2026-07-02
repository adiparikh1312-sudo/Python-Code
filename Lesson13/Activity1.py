print("Printing a half pyramid(*)")
n = int(input("How many rows do you want?"))

for i in range(n):
    for j in range (i+1):
        print("*", end = " ")
    
    print()
