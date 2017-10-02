import random
user_password = input('give me a number from 6 to 16 ')
pw_int =int(user_password)
letters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mypw = ""
number = ""

for i in range(pw_int):
    next_index = random.randrange(len(letters))
    mypw = mypw + letters[next_index]

print(mypw)

