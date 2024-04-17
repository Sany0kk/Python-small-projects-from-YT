import random

WORD1 = int(input("Enter the starting number: "))
WORD2 = int(input("Enter the ending number: "))
print(f"Your starting point is {WORD1} and ending point is {WORD2}! ")
number_generated = random.randint(WORD1,WORD2)
count_machine = 0

while True:
    try:
        guess = int(input("Enter your guess!: "))
    except ValueError:
        print("Enter the valid integer: ")
        continue
    count_machine += 1

    if guess == number_generated:
        print("Correct! It took you", count_machine, "tries to guess the number.")
        break
    if (guess + 1 or guess - 1) == number_generated:
        print("Your guess is so close! ")
    elif guess > number_generated:
        print("Your guess is bigger than the actual number! ")
    elif guess < number_generated:
        print("Your guess is smaller than the actual number! ")
    else:
        print("Try again")