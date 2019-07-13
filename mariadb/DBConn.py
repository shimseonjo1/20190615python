import pymysql as my

def loginSQL(uid, upw):
    conn = my.connect(
        host='127.0.0.1',
        user='root',
        password='1234',
        db='test',
        charset='utf8',
        port=3306,
        cursorclass=my.cursors.DictCursor
    )

    try:
        with conn.cursor() as cursor:
            query = """
                select * from user where uid=%s and upw=%s
            """
            cursor.execute(query,(uid, upw))
        result = cursor.fetchone()

        return result
    finally:
        conn.close()


