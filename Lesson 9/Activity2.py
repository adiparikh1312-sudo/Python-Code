units = float(input("No. of units used: "))

if (units < 50):
    amount = (units * 2.60)
    surcharge = 25

elif (units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif (units <= 200):
    amount = 130 + 162.5 + ((units - 100) * 5.26)
    surcharge = 45

else: 
    amount = 130 + 162.5 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge

print("\n Your electricity bill is %.2f, for %.2f units"% (total, units))