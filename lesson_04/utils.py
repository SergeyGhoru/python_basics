import requests
import json
from datetime import datetime

def currency_rates(c: str):
    """
    Input: string with calute code ('USD' or 'GBP')
    Output: dictionary
    {'date': <class 'datetime.datetime'>, rate': float}
    """
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL)
    currencies = json.loads(response.text)
    code = c.upper()
    dt = datetime.strptime(currencies['Date'],'%Y-%m-%dT%H:%M:%S%z')
    try:
        return {'date': dt, 'rate': currencies['Valute'][code]['Value']}
    except KeyError:
        return None

if __name__ == "__main__":
    pass
