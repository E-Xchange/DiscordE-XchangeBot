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


currency_start_time = ["09:00", "13:00", "15:00", "19:00"]
for i in currency_start_time:
    schedule.every().day.at(i).do(currency_start, 'currency-start')

crypto_start_time = ['09:00', '10:00', '11:00', '12:00', '14:00', '15:00',
                     '16:00', '17:00', '19:00', '20:00', '22:00', '00:00']
for i in currency_start_time:
    schedule.every().day.at(i).do(crypto_start, 'crypto-start')

metals_start_time = ['10:30', '19:30']
for i in currency_start_time:
    schedule.every().day.at(i).do(metals_start, 'metals-start')

while True:
    schedule.run_pending()
    time.sleep(60)
