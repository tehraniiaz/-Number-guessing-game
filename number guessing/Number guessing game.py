import random
number=input("guess your number:")
number=int(number)

guess=random.randint(1,99)
print(guess)

while number != guess:
    if(guess>number):
        print("guess is larger")
    else:
        print("guess is smaller")
    number=int(input("guess your number:"))
print("thanks your guess is correct")