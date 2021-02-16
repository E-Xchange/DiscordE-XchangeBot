import config.time_cfg as cfg
import os
import schedule
import time


def currency_start(time):
    print("I'm working (currency)", time)
    os.system('python currencyinfo.py')
    return


def crypto_start(time):
    print("I'm working (crypto)", time)
    os.system('python cryptoinfo.py')
    return


def metals_start(time):
    print("I'm working (metals)", time)
    os.system('python metalsinfo.py')

    return


for i in cfg.currency_start_time:
    schedule.every().day.at(i).do(currency_start, 'currency-start')

for i in cfg.crypto_start_time:
    schedule.every().day.at(i).do(crypto_start, 'crypto-start')

for i in cfg.metals_start_time:
    schedule.every().day.at(i).do(metals_start, 'metals-start')

while True:
    schedule.run_pending()
    time.sleep(60)
