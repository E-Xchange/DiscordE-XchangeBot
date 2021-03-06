import mariadb

SQLdb = mariadb.connect(
    host="127.0.0.1",
    user="test",
    password="test",
    database="exchange",
)


def addmetals(price, type):
    mycursor = SQLdb.cursor()
    sql = "INSERT INTO metals (price, type) VALUES (%s, %s)"
    val = (price, type)
    mycursor.execute(sql, val)
    SQLdb.commit()


def addcrypto(price, type):
    mycursor = SQLdb.cursor()
    sql = "INSERT INTO crypto (price, type) VALUES (%s, %s)"
    val = (price, type)
    mycursor.execute(sql, val)
    SQLdb.commit()


def addcurrency(price, type):
    mycursor = SQLdb.cursor()
    sql = "INSERT INTO currency (price, type) VALUES (%s, %s)"
    val = (price, type)
    mycursor.execute(sql, val)
    SQLdb.commit()


def takeprice(type):
    mycursor = SQLdb.cursor()
    # TODO: cut this line
    mycursor.execute(f"SELECT price, type FROM {type} WHERE date=(SELECT MAX(date) FROM {type})")
    return mycursor.fetchall()


def adddiscordid(discordid):
    mycursor = SQLdb.cursor()
    sql = "INSERT INTO notification (dcid) VALUES (%s)"
    val = (discordid, )
    mycursor.execute(sql, val)
    SQLdb.commit()


def removediscordid(discordid):
    mycursor = SQLdb.cursor()
    sql = "DELETE FROM notification WHERE (dcid=%s)"
    val = (discordid, )
    mycursor.execute(sql, val)
    SQLdb.commit()


def takediscordid():
    mycursor = SQLdb.cursor()
    mycursor.execute("SELECT dcid FROM notification")
    return mycursor.fetchall()


def takeLastBtc():
    mycursor = SQLdb.cursor()
    mycursor.execute(
        f"SELECT date, price FROM crypto WHERE type = 'BTC' ORDER BY date DESC LIMIT 1;")
    temp = mycursor.fetchone()
    today_price_real, yesterday_time_check = temp[1], temp[0] - 85400

    sql = (
        f"SELECT date, price FROM crypto WHERE type='BTC' AND (date<%s) ORDER BY date DESC LIMIT 1")
    val = (yesterday_time_check, )
    mycursor.execute(sql, val)

    mycursor_data = mycursor.fetchone()
    yesterday_price_real = mycursor_data[1]

    return today_price_real, yesterday_price_real
