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

data_EUR = open_url_EUR.read()
json_data_EUR = json.loads(data_EUR)

data_AUD = open_url_AUD.read()
json_data_AUD = json.loads(data_AUD)

data_CHF = open_url_CHF.read()
json_data_CHF = json.loads(data_CHF)

base_USD_price = json_data_USD['rates'][0]['mid']
EUR_price = json_data_EUR['rates'][0]['mid']/base_USD_price
AUD_price = json_data_AUD['rates'][0]['mid']/base_USD_price
CHF_price = json_data_CHF['rates'][0]['mid']/base_USD_price

print(round(EUR_price, 2))
print(round(AUD_price, 2))
print(round(CHF_price, 2))
