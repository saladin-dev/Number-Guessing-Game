import random
guess=15
number = 0
guess_counter = 0

while guess != number:
    number = random.randint(0, 10)
    guess = int(input("pick a # between 0-10 "))
    guess_counter += 1
    print ("This how many guesses you have:", guess_counter)
    if guess != number:
        print(f"Wrong! The correct number was {number}.")
    else:
        break

print(f"You guessed the number:", number)
