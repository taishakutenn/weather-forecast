import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = '7e3acd940fe24b11064b66352e81b0b5'


def find_weather():
    city = input('Введите название города: ')

    params = {'q': city,
              'units': 'metric',
              'lang': 'ru',
              'appid': api_key
             }

    responce = requests.get(url, params=params)
    result = responce.json()
    print(f'Город: {city}')
    print(f'Температура на улице: {result['main']['temp']}°\nОщущается как: {result['main']['feels_like']}°')
    print(f'На улице: {result['weather'][0]['description']}')
    print(f'Скорость ветра: {result['wind']['speed']} м/c')


while True:
    working = input()

    if working == 'find weather':
        find_weather()
        break