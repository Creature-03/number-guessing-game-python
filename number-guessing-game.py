import random
import math

#inputs
lower = int(input("Enter lowest possible number."))
upper = int(input("Enter highest possible number."))

#generates random number between $lower and $upper
random_number = random.randint(lower, upper)

#generates max number of guess attempts
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou have ", total_chances, " chances to guess the number!\n")

#initializes the number of guesses
guess_count = 0
flag = False

#creates game logic and increases $guess_count each guess
while guess_count < total_chances:
    guess_count += 1

    #gets user input
    guess = int(input("Guess a number: "))

    #tests $guess against $random_number
    if random_number == guess:

        #alters victory text if the user guesses corrects the first guess
        if guess_count == 1:
            print("Congratulations! You've guessed the number on your first try!")
            flag = True
            break
        #alters victory text if the user guesses correctly after multiple attempts
        else:
            print("Congratulations! you've guessed the number in ", guess_count, " guesses!")
            flag = True
            break
    
    #alerts the user if $guess is lower than $random_number
    elif random_number > guess:
        print("You've guessed too low, try higher!")

    #alerts the user if $guess is higher than $random_number
    elif random_number < guess:
        print("You've guessed too high, try lower!")

#alerts the user and ends the game when $guess_count exceeds $total_chances
if not flag:
    print("\nThe number is %d \n\t Better luck next time!" % random_number)
