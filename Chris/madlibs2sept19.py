
# user_1 = input ('give me an adjective, ')
# user_2 = input ('give me an noun ')
# user_3 = input ('give me an plural noun ')
# user_4 = input
#
# print(user_1, ' ', user_2, ' ',user_3 )
# print ('there are many, ', user_1,'ways to choose, ',user_2, 'to read ,First you could ask for recommendations from your friends and, ',user_3)

nouns = input('5nouns')

nounlist = nouns.split(',')
if len(nounlist) == 5:
    print(nounlist[0])
    print(nounlist)
    print(nounlist[0], nounlist[1], nounlist[2], nounlist[3], nounlist[4])
else:
    print('error start again')


