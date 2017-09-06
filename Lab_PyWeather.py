import requests

package = {'APPID': "6dca459da0817a2f599a0bb6662f8912", "q":"portland"}

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

data = r.json()
print(data)
