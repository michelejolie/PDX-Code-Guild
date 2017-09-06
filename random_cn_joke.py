import requests
r = requests.get ('http://api.icndb.com/jokes/random')
data = r.json()

print('Joke #{}'.format(data['value']['id']))
print('{}'.format(data['value']['joke']))

