# #### Goal
#
# Create a program asks for a _single_ English word and translates
# it to **Pig Latin**.
# It prints out the input word and the resulting translation like
# the example below.
#
# ---------------------------------
#
# #### Instructions
#
# 1. If the first letter is a consonant, move it to the end.
# 1. Add "ay" to the end of that.
# 1. If the first letter is a vowel, just ad "yay" to the end.


# get a word from user
word = input('What word would you like translated?: ')
# split first letter from word so we have two parts
vowels = 'aeiou'
consonant = -1

for letter in word:
    if letter.lower() in vowels:
        break
    else:
        consonant += 1

first_letter = word[0:consonant + 1]
left_over = word[consonant + 1:]

# list vowels
# compare first letter to list of vowels
if first_letter.lower() in vowels:
    # if true add word + 'yay'
    print('{0} in Pig Latin is {0}yay'.format(word))
# else move first letter to the end of word and add 'ay'
else:
    if first_letter[0].isupper():
        print('{0} in Pig Latin is {1}{2}ay.'.format(word, left_over.capitalize(), first_letter.lower()))
    else:
        print('{0} in Pig Latin is {1}{2}ay.'.format(word, left_over, first_letter))
