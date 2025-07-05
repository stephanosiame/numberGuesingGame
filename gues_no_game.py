import random

print ("Hi! Welcome to the number guesing Game. \n You have the seven 7 chance to guess the number. Let start")

low = int(input ("Enter The Lower bound"))
high = int (input ("Enter The Upper Bound"))

print(f"You have 7 Chance to choose the number between {low} and {high}. Let start")

num = random.randint(low, high)

ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("enter Your guess"))

    if guess == num:
        print(f"Correct! The number is {num}. Your guessed it in {gc} attempt.")
        break

    elif gc >= ch and guess != num:
        print(f"sorry! the number was {num}. Better Luck next time")

    elif guess > num:
        print("Too high. You may try the lower number")

    elif guess < num:
        print("Too Low. You may try higher number")