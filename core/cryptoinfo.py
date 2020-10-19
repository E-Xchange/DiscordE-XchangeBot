import json, os
import urllib.request
from core.databasemodule import addcrypto
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('crypto_link')
open_url = urllib.request.urlopen(url)

data = open_url.read()
json_data = json.loads(data)

bitcoin_price = round(json_data['BTC']['USD'], 2)
ethereum_price = round(json_data['ETH']['USD'], 2)
cardano_price = round(json_data['ADA']['USD'], 2)


addcrypto(bitcoin_price, 'BTC')
addcrypto(ethereum_price, 'ETH')
addcrypto(cardano_price, 'ADA')

