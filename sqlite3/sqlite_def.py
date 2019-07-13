import sqlite3

#테이블 생성 함수
def create_table():
    conn=sqlite3.connect('sqlite3/my_books.db')
    cursor=conn.cursor()
    #my_books테이블 생성(제목,출판일자,출판사,페이지수,추천여부)
    cursor.execute('''create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
        )''')
    conn.commit()
    conn.close()



#데이터 입력 함수
def insert_books(items):
    conn=sqlite3.connect("sqlite3/my_books.db") #db연결
    cursor=conn.cursor()
    #데이타 입력방법1
    #cursor.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    #데이타 입력방법2
    sql='insert into books values(?,?,?,?,?)'
    #cursor.execute(sql,('Python','201001','한빛',584,20))
    #데이타 입력방법3
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()



#전체 데이터 출력 함수
def all_books():
    conn=sqlite3.connect("sqlite3/my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    print('[1] 전체 데이터 출력하기')
    books=cursor.fetchall()
    print(type(books))
    print(len(books)) #레코드 개수 출력

    for book in books:
        for i in book:
            print(i,end=" ")
        print()

    conn.close()




#레코드 개수 정하여 출력
def some_books(number):
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    books=cursor.fetchmany(number)

    for book in books:
        for i in book:
            print(i,end=" ")
        print()
    
    conn.close()




#1개의 데이타 출력하는 함수
def one_book():
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    book=cursor.fetchone()
    print(type(book))
    print(book)
    conn.close()




#조건 지정 및 정렬하여 검색
def big_books():
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    #페이지수가 300이상이고 페이지수가 많은 순서대로 title,page 출력
    cursor.execute('''select title,pages from books
                    where pages>300 order by pages desc''')
    books=cursor.fetchall()

    for book in books:
        for i in book:
            print(i,end=" ")
        print()

    conn.close()




# 데이터 수정 함수
def update_books():
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    #title이 java인 recommend를 200으로 수정
    sql='''update books 
            set recommend=? where title=?'''
    sql='''update books
            set recommend=:1 where title=:2'''
    cursor.execute(sql,(200,'Java'))
    conn.commit()
    conn.close()




#데이터 삭제 함수
def delete_books():
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    #publisher가 한빛인 데이터 삭제
    sql="delete from books where publisher='한빛'"
    cursor.execute(sql)
    # sql="delete from books where publisher=:1"
    # cursor.execute(sql,('한빛',))
    conn.commit()
    conn.close()


