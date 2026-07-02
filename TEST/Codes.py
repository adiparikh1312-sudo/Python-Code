import random

playing = True

while playing:
    try:
        user_number = int(input("Enter a number from 10 to 20: "))
        computer_number = random.randint(10, 20)

        if user_number == computer_number:
            print("You guessed the number right, you win")
            print("The number was", computer_number)
        else:
            print("You lose.")
            print("The number was", computer_number)

        playing = False

    except ValueError:
        print("Please enter a valid number.")



try:
    def is_palindrome(word):
        clean_word = word.lower()
        return clean_word == clean_word[:: -1]

    word = (input("Enter a word:"))
    if is_palindrome(word) == True:
        print("Your word is a palindrome")
    elif is_palindrome(word) == False:
      print("Your word is not a palindrome")

except ValueError:
    print("Enter a word, not any other character")


def area_of_parallelogram(base, height):
    return base * height 

base = int(input("Enter the base of the parallelogram(in cm):"))
height = int(input("Enter the height of the parallelogram (in cm):"))

print("The area of your parallelogram is,", area_of_parallelogram(base, height))

def add(x, y):
    return x + y

print(add(5, 6))

def subtract(x, y):
    return x - y

print(subtract(6, 5))