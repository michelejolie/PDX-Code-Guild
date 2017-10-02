
import random
eyeballs = True
while eyeballs:
    user = input("would you like to have some fun? " )

    if user == 'yes':
        print(" did you made me smile?")

        list_of_eyes = [';', ':', ]

        list_of_noses = ['-', '=']

        list_of_lips = [')', '(','p']

        eyes = random.choice(list_of_eyes)
        noses = random.choice(list_of_noses)
        lips = random.choice(list_of_lips)
        print(eyes,noses,lips)

    if user == 'no':
        eyeballs = False
        print("Thank you come back again")