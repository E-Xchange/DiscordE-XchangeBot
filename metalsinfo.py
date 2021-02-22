from left import price_PT, price_AG, price_AU
from databasemodule import addmetals

addmetals(price_AU, 'gold')
addmetals(price_AG, 'silver')
addmetals(price_PT, 'platinum')
