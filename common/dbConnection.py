import pymysql
from common.constant import Constant

class DbConnection():
    def __init__(self, sql):
        self.sql = sql

    def connect(self):
        connection = pymysql.connect(host=Constant.DB_HOST, port=Constant.DB_PORT, user=Constant.DB_USER,
                                     passwd=Constant.DB_PASSWD, db=Constant.DB_DB, charset=Constant.DB_CHARSET)
        cursor = connection.cursor()
        result = ""
        try:
            cursor.execute(self.sql)
            result = cursor.fetchall()
        except:
            print("sql语句出错！")
        connection.close()
        return result