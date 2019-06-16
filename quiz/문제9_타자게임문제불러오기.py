import random
import time

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
while True:
   print("1.문제불러오기  2.타자게임  3.등수저장하기")
   menu = input("메뉴를 선택하세요")
   if menu=='1':
       f=open('word.txt','r')

   n=1
   print("[타자 게임]준비되면 엔터!")
   input()
   start=time.time()
   q=random.choice(w)
   while n<=5:
      print("*문제",n)
      print(q)
      x=input()
      if q ==x:
         print("통과!")
         n=n+1
         q=random.choice(w)
      else:
         print("오타! 다시도전!")
   end =time.time()
   et=end-start
   et=format(et,".2f")
   print("타자 시간 : ",et,"초")