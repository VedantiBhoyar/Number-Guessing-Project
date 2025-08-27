import random

from art import logo

print(logo)
print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type easy or hard").strip().lower()

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def guess_number(numbers_of_attempts):
    number = random.randint(1, 101)
    user_guess = 0
    while numbers_of_attempts > 0 and number != user_guess:
        print(f"You have {numbers_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess : "))
        if user_guess == number:
            hints(number,user_guess)
        else:
            numbers_of_attempts -= 1
            hints(number,user_guess)

def hints(number,user_number):
    if user_number > number:
     print("You guessed incorrectly , Number too high")
    elif user_number<number:
        print("You guessed incorrectly , Number is too low")
    elif user_number == number:
        print("You guess the number correctly")


if difficulty == "easy":
    guess_number(EASY_ATTEMPTS)
else:
    guess_number(HARD_ATTEMPTS)
