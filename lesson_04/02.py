import requests
import json


# GET moved out of fucntion to reduce the frequency of requests
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL)
currencies = json.loads(response.text)


def currency_rates(c: str):
    """
    Input: string with calute code ('USD' or 'GBP')
    Output: float - exchange rate RUR to valute
    """
    code = c.upper()
    try:
        return currencies['Valute'][code]['Value']
    except KeyError:
        return None


print(currency_rates('USD'))
print(currency_rates('gbp'))
print(currency_rates('adsf'))
