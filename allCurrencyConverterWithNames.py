import requests

userInput = input(f'Type an amount and the currencies (or a currency and a country) you wish to convert between e.g. '
                  f'"300 USD EUR": ')
if len(userInput.split(' ')) == 3:
    try:
        amount = float(userInput.split(' ')[0])
    except ValueError:
        print('Amount must be numbers only!')
        amount = 1
    fromCurrency = userInput.split(' ')[1].upper()
    toCurrency = userInput.split(' ')[2].upper()

    if len(fromCurrency) > 3:
        file = open("currency_codes.txt", "r")
        for line in file.readlines():
            if line.split("\t")[0].__contains__(fromCurrency.upper()):
                fromCurrency = line.split("\t")[2]
                file.close()
                break
    if len(toCurrency) > 3:
        file = open("currency_codes.txt", "r")
        for line in file.readlines():
            if line.split("\t")[0].__contains__(toCurrency.upper()):
                toCurrency = line.split("\t")[2]
                file.close()
                break

    response = requests.get(f'https://open.er-api.com/v6/latest/{fromCurrency}')

    if response.json()['result'] != 'error':
        rates = response.json()['rates']
        try:
            print(f'{fromCurrency}: {amount} -> {toCurrency}: {round(amount * rates[toCurrency], 2)}')
            # print(f'Rates correct at {response.json()["time_last_update_utc"]}.')
        except KeyError:
            print('The destination currency was not found.')

    else:
        print('The conversion could not be completed.')

else:
    print('Usage: {amount} {from} {to}')
