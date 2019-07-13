# 함수화 처리
# 아이디, 비번을 인자로 입력 받아서, 재활용성을 높이고, 모듈화의 모양새를 갖춘다.
import pymysql as my

# 키워드를 이용하여 이름에 해당 키워드가 포함된 프로젝트 목록을 리턴한다.
def selectProjectByKeyword(keyword):
    connection=None
    rows=None # 해당 정보를 가져오는 변수
    try:
        connection=my.connect(host='127.0.0.1',
                                user='root',
                                password='qwer1324',
                                db='test',
                                charset='utf8',
                                port=3306,
                                cursorclass=my.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql='''
                select * from 