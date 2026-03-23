a = int(input("Enter value 1 (integer):"))
b = int(input("Enter value 2 (integer):"))
c = int(input("Enter value 3 (integer):"))

avg = (a + b + c)/3

print (avg)

if avg > a and avg > b and avg > c:
    print(avg, "is greater than", a, b, c)
elif avg > a and avg > b:
    print(avg, "is greater than", a, b)
elif avg > b and avg > c:
    print(avg, "is greater than", b, c)
elif avg > a and avg > c:
    print(avg, "is greater than", a, c)
elif avg > a:
    print(avg, "is greater than", a)
elif avg > b:
    print(avg, "is greater than", b)
elif avg > c:
    print(avg, "is greater than", c)
else:
    print(" Invalid Input!")

