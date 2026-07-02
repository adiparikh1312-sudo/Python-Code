def factorial(x):
    ' ' ' this is a recursive function o find the factorial of an integer ' ' '

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)


print(factorial.__doc__)
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 4:", factorial(4))
print("the factorial of 5:", factorial(5))
print("The factorial of 100:", factorial(100))

