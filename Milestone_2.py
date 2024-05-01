# Omran Adam 
# Milestone 2
# 04/21/2024
#-------------------------------------------------------------------------------------------------
import random # import random
random_number = random.randint(1,100) # store random number using random libary 
name = input("Enter your name: ") # prompt user to enter their name
counter = 0                         # creat counter for the guess
print(f"{name}, the Guardian commands you to unravel the riddle! Guess a number between 1 and 100!")
while counter < 6:      #  Create a loop that gives the user 6 attempts to guess the number. #
    guess = int(input("Enter a number: "))
    counter+=1
    if guess < random_number:   # this statement check whether the guess is less the random_number
        print("That guess is too low")
    elif guess > random_number:
        print("That guess is too high")

    else:
        print(f"Congratulations, {name}, you guess a number in {random_number} attempt!")

if counter == 6 and guess != random_number:
    print(f"Sorry, {name} you out of the attemp. The correct number is {random_number}")
#------------------------------------------------------------------------------------------------------------









