import random
# Lab 9: Guess the Number
# Let's play 'Guess the Number', the computer will guess a random int between 1 and 10. The
# Version 1
# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost.
# Version 2
# Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
# Version 3
# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
# Version 4
# Tell the user whether their current guess is closer than their last.
# Version 5
# Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.
#user will then try to guess the number, and the program will tell them whether they're right or wrong.

print("Let's play a game"  "," " pick a number from" "," " 1 - 10 ")
guesses = 10
guess = 0
while guess < guesses:
    guess += 1
    user_input = input('give me a number from 1 to 10 ')

    user_int = int(user_input)

    computer = random.randint(1,10)

    if user_int == computer:
        guess = guesses
        print('you win')

