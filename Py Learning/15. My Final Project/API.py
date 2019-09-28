import urllib.request
import json
import textwrap

city = 'london'
apiLink = f'https://samples.openweathermap.org/data/2.5/weather?q={city},uk&appid=b6907d289e10d714a6e88b30761fae22'
with urllib.request.urlopen(apiLink) as f:
    text = f.read()
    decodedText = text.decode('UTF-8')
    # print(textwrap.fill(decodedText, 50))

obj = json.loads(decodedText)
coord = obj['coord']
weather = obj['weather'][0]
print(f"Longitude {coord['lon']}")
print(f"Latitude {coord['lat']}")
print(weather['id'])
print('Short Desc:',weather['main'])
print('Description:',str(weather['description']).capitalize())
