from common.dbConnection import DbConnection

class DbTest():

    sql = "select name,passwd from t_user where id=1"
    db_connection = DbConnection(sql)
    result = db_connection.connect()
    print(result)
    print(result[0])
    print(result[0][0])
