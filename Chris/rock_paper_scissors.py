import random
user = input('what would you like to pick? ')
kids_game = ['rock', 'scissors', 'paper']
kids_choice = random.choice(kids_game)

print(kids_choice)
print(user + ',' + kids_choice)
if user == kids_choice:
    print('draw')
if user == "rock" and kids_choice == "paper":
    print("you loser")
if user == "paper" and kids_choice == "scissors":
    print("you win this timer")
if user == "scissors" and kids_choice == "rock":
    print("I lose this time joker")

#making a wild loop
