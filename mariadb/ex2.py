# cos DB연결
import pymysql
import json

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='qwer1324', db='test', charset='utf8')
# 커서 만들기
cursor = db.cursor()
# """ """ 이 안에서는 문자열을 편하게 작성가능
# 테이블 생성

# sql = """
#     create table baseball(
#         id int,
#         name varchar(20)
#     )
# """

# 데이터 넣기
sql = """
    insert into baseball values(1,'cos')
"""
cursor.execute(sql)

# 데이터 검색
sql = """
    select * from baseball
"""

cursor.execute(sql)
#cursor.execute("show tables")
#db.commit()

rs = cursor.fetchall()
print(rs)

rs_dict = dict(rs)
print(rs_dict)

# type이 str이라도 dumps를 해서 보내줘야 한다.
# json으로 변경해야함.
rs_json = json.dumps(rs_dict)
print(type(rs_json))
print(rs_json)


