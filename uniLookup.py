import requests


country = input('Type a country to look up its universities: ')

response = requests.get(f'http://universities.hipolabs.com/search?country={country}')

unis = response.json()

i = 0

for uni in unis:
    i += 1
    try:
        print(uni['name'])
    except KeyError:
        continue

print(f'Count: {i}')

