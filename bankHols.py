import requests

# default country code
countryCode = 'england-and-wales'
userResponse = input('Enter the country you want Bank Holidays for e.g. "England": ')
response = requests.get('https://www.gov.uk/bank-holidays.json')

if userResponse == 'England' or userResponse == 'Wales':
    countryCode = 'england-and-wales'
elif userResponse == 'Scotland':
    countryCode = 'scotland'
elif userResponse == 'Northern Ireland':
    countryCode = 'northern-ireland'

print(countryCode)
events = response.json()[f'{countryCode}']['events']
for event in events:
    if '2024' in event['date']:
        print(f'{event["title"]} - {event["date"]}')
