import sqlite3

conn=sqlite3.connect('sqlite3/example.db')
c=conn.cursor()
symbol='aaa'
c.execute("select * from stocks where symbol='%s'" %symbol)
itmes = c.fetchall()

for item in itmes:
    print(item)



t=('RHAT',)
sql='select * from stocks where symbol=?'
c.execute(sql,t)
print(c.fetchall())
