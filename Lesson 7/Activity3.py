print("All marks should be a whole number and they should be out of 100")

Mark1 = int(input("Please enter your marks of English:"))
Mark2 = int(input("Please enter your marks of Math:"))
Mark3 = int(input("Please enter your marks of Science"))
Mark4 = int(input("Please enter your marks of Spanish:"))
Mark5 = int(input("Please enter your marks of History/Geography:"))

tot = Mark1 + Mark2 + Mark3 + Mark4 + Mark5
print("Your total number of marks is", tot)

avg = tot/5
print("Your average of marks is", avg)

if avg >= 91 and avg <= 100:
    print("Your grade is A+. Congratulations!")
elif avg >= 81 and avg < 91:
    print("Your grade is A. Congratulations!")
elif avg >= 71 and avg < 81:
    print("Your grade is B+. Well Done!")
elif avg >= 61 and avg < 71:
    print("Your grade is B. Well Done!")
elif avg >= 51 and avg < 61:
    print("Your grade is C+. You can do better.")
elif avg >= 41 and avg < 51:
    print("Your grade is C. You can do better.")
elif avg >= 33 and avg < 41:
    print(" Your grade is D+. You should study a lot more.")
else:
    print("FAIL.")

print("The above are your exam results")
