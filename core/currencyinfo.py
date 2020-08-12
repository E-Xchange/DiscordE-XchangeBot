from requests import Request
import json
import urllib

url_USD = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/'
url_EUR = 'http://api.nbp.pl/api/exchangerates/rates/a/eur/'
url_AUD = 'http://api.nbp.pl/api/exchangerates/rates/a/aud/'
irl_CHF = 'http://api.nbp.pl/api/exchangerates/rates/a/chf/'

open_url_USD = urllib.request.urlopen(url_USD)
open_url_EUR = urllib.request.urlopen(url_EUR)
open_url_AUD = urllib.request.urlopen(url_AUD)
open_url_CHF = urllib.request.urlopen(irl_CHF)

data_USD = open_url_USD.read()
json_data_USD = json.loads(data_USD)
base_USD_price = json_data_USD['rates'][0]['mid']


def data(url_open):
    data = url_open.read()
    json_data = json.loads(data)
    price = json_data['rates'][0]['mid']/base_USD_price
    print(round(price,2))


data(open_url_EUR)
data(open_url_AUD)
data(open_url_CHF)

