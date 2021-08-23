import pymysql
import pymysql.cursors

def getMysqlConnection():
    connection = pymysql.connect(
        host='test.com',
        port=3306,
        user='localhost',
        password='1234',
        db='short_url',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection
