import sqlite3

def create_table():
    conn=sqlite3.connect('employee.db')
    cursor=conn.cursor()
    sql='''create table if not exists employees(
        eno integer,
        ename text,
        dname text,
        position text,
        salary integer
    )'''
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert_one(t):
    conn=sqlite3.connect('employee.db')
    cursor=conn.cursor()
    sql='insert into employees values(?,?,?,?,?)'
    cursor.execute(sql,t)
    conn.commit()
    conn.close()

def all_employees():
    conn=sqlite3.connect('employee.db')
    cursor=conn.cursor()
    cursor.execute('select * from employees')
    employees=cursor.fetchall()

    for employee in employees:
        for i in employee:
            print(i,end=" ")
        print()

    conn.close()

def update_employees(t):
    conn=sqlite3.connect('employee.db')
    cursor=conn.cursor()
    sql='''update employees
            set dname=:1, position=:2,salary=:3
            where eno=:4'''
    cursor.execute(sql,t)
    conn.commit()
    conn.close()

def delete_employees(t):
    conn=sqlite3.connect('employee.db')
    cursor=conn.cursor()
    sql='delete from employees where eno=?'
    cursor.execute(sql,t)
    conn.commit()
    conn.close()


