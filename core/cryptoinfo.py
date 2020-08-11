from requests import Request
import json
import urllib

url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,DASH,BTC&tsyms=BTC,USD,EUR&api_key=55599765b9bb94391e2788c60fe9663e0e0eb6cfbb8f0ebf0fe08d4ca'
open_url = urllib.request.urlopen(url)


data = open_url.read()
json_data = json.loads(data)

bitcoin_price = round(json_data['BTC']['USD'])
ethereum_price = round(json_data['ETH']['USD'])
cardano_price = round(json_data['ADA']['USD'])
