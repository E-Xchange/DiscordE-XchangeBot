import json, os
import urllib.request
from core.databasemodule import addcrrency
from dotenv import load_dotenv

load_dotenv()
url_USD = os.getenv('nbp_link_usd')
url_EUR = os.getenv('nbp_link_eur')
url_AUD = os.getenv('nbp_link_aud')
url_CHF = os.getenv('nbp_link_uchf')

open_url_USD = urllib.request.urlopen(url_USD)
open_url_EUR = urllib.request.urlopen(url_EUR)
open_url_AUD = urllib.request.urlopen(url_AUD)
open_url_CHF = urllib.request.urlopen(url_CHF)

data_USD = open_url_USD.read()
json_data_USD = json.loads(data_USD)
base_USD_price = json_data_USD['rates'][0]['mid']


def data(url_open):
    data = url_open.read()
    json_data = json.loads(data)
    price = json_data['rates'][0]['mid'] / base_USD_price
    return (round(price, 2))


USD_EUR_price = data(open_url_EUR)
USD_AUD_price = data(open_url_AUD)
USD_CHF_price = data(open_url_CHF)

addcrrency(USD_EUR_price, 'EUR')
addcrrency(USD_AUD_price, 'AUD')
addcrrency(USD_CHF_price, 'CHF')
