print("Enter Marks obtained of 4 subject:")
math = int(input())
science = int(input())
english = int(input())
spanish = int(input())

sum = math + science + english + spanish
print("The sum of the scores is:", sum)

perc = (sum / 400) * 100
print(end="The percentage is :")
print(perc)
