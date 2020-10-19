import mariadb

SQLdb = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="piotr2002",
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

def addcrrency(price, type):
    mycursor = SQLdb.cursor()
    sql = "INSERT INTO currency (price, type) VALUES (%s, %s)"
    val = (price, type)
    mycursor.execute(sql, val)
    SQLdb.commit()
