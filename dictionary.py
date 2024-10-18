import requests

userWord = input('Type a word to find the meaning(s): ')

response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{userWord}')

try:
    meanings = response.json()[0]['meanings']
    for meaning in meanings:
        print(meaning['partOfSpeech'].upper())
        definitions = meaning['definitions']
        for definition in definitions:
            print(definition['definition'])
except KeyError as ke:
    print(response.json()['title'])
