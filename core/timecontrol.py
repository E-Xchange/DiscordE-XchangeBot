import os
import schedule
import time

def currencystart(time):
    print("I'm working...", time)
    os.system('python currencyinfo.py')
    return

array = ["09:00","13:00","15:00", "19:00"]
for i in array:
    schedule.every().day.at(i).do(currencystart,'currency-start')

while True:
    schedule.run_pending()
    time.sleep(60)


