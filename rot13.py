from string import ascii_uppercase, ascii_lowercase

upper = ascii_uppercase*2
lower = ascii_lowercase*2

def rotate(message, amount):
    new_message = ""
    for letter in message:
        if letter in upper:
            new_message += upper[upper.index(letter) + amount]
        elif letter in lower:
            new_message += lower[lower.index(letter) + amount]
        else:
            new_message += letter
    return new_message

print(rotate(input("Message: "), 13))
