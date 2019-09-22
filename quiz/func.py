import time,random

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
rank={}

def sortV(x):
    return x[1]

def openRank():
    f = open('rank.txt', 'r',encoding='UTF8')
    line = 1
    while line:
        line = f.readline().replace("\n", "")
        if not (line == ''):
            k, v = line.split(':')
            rank[k] = float(v)

def closeRank():
    f = open('rank.txt', 'w', encoding='UTF8')
    text = ''
    items = rank.items()
    for k, v in items:
        text = text + k + ':' + str(v) + '\n'
    f.writelines(text)
    f.close()    

def quizOpen():
    f=open('word.txt','r',encoding='UTF8')
    line = 1
    w.clear()
    while line:
        line = f.readline().replace("\n","")
        if not(line==''):
            w.append(line)
    print(w)

def quiz():
    n=1
    q=random.choice(w)
    input('시작!')
    start = time.time()
    while n<=5:
        print("{}번".format(n))
        print(q)
        x=input()
        if q ==x:
            print("통과!")
            n=n+1
            q=random.choice(w)
        else:
            print("오타! 다시도전!")  
    end= time.time()
    print('타자 시간 : {:.0f}초'.format(end-start))    
    name = input("사용자 이름을 입력하세요")
    rank[name]=float(end-start)

def rankList():
    ranklist=sorted(rank.items(),key=sortV)
    num=1
    for k,v in ranklist:
        print("%d등 %s %f" %(num,k,v))
        num = num+1