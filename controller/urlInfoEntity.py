
def find(baseUrl, mysqlConnection):
    cursor = mysqlConnection.cursor()

    query = "SELECT * FROM url_info WHERE TargetURL = %s"
    cursor.execute(query, (baseUrl))
    data = cursor.fetchone()

    return data
