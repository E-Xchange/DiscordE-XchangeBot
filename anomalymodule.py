from databasemodule import takeLastBtc


def checkAnomaly():
    data = takeLastBtc()

    result = (round(float(data[0])/float(data[1])*100-100, 2))

    if result >= 10:
        return result, True

    return result, False
