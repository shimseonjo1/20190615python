import dao

eno=int(input('사번입력 : '))
ename=input('사원명 입력 : ')
dname=input('부서명 입력 : ')
position=input('직급 입력 : ')
salary=int(input('급여 입력 : '))
t=(eno,ename,dname,position,salary)
dao.create_table()
dao.insert_one(t)
dao.all_employees()
dao.update_employees(('홍보부','과장',500,3))
dao.all_employees()
dao.delete_employees((3,))
dao.all_employees()