char = input("Enter a character (one digit only): ")

code = ord(char)

if (code >= 65 and code <= 90) or (code >= 97 and code <= 122):
    print("It is an alphabet")
else:
    print("It is not an alphabet")

