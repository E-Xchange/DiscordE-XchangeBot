from databasemodule import takeLastBtc


def checkAnomaly():
    data = takeLastBtc()

    resault = (round(float(data[0])/float(data[1])*100-100, 2))

    status = False
    if resault >= 10:
        status = True

    return resault, status
