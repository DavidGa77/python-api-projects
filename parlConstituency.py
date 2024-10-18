import requests

print('Find your parliamentary constituency')
postcode = input(f'Please enter your postcode including the space: ')
response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')

if response.status_code == 200:
    print(response.json()['result']['parliamentary_constituency'])
else:
    print(response.json()['error'])
