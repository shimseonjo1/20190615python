import random,time,pickle

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
rank={}

def rankLoad():
    with open('./quiz/rank.pkl','rb') as f:
        rank=pickle.load(f)

def wordLoadTxt():
    f=open('./quiz/word.txt','r',encoding='utf8')
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].replace('\n','')
        w=w+lines 
    print(w)
    f.close()
    '''
    f=open('./quiz/word.txt','r',encoding='utf8')
    line = 1
    while line:
        line = f.readline().replace("\n","")
        if not(line==''):
        w.append(line)
    print(w)
    f.close()
    '''

def wordSaveTxt():
    f=open('./quiz/word.txt','w',encoding='utf8')
    for i in w:
        data=''
        data+=i+'\n'
        f.write(data)
    f.close()

def wordAppend():
    quiz=1
    while quiz:
        quiz=input('추가할 단어 입력(종료:0) >> ')
        if quiz=='0':
            print('입력을 종료합니다.')
            break
        w.append(quiz)
    print(w)

def wordSavePik():
    with open('./quiz/pickle.pkl','wb') as f:
        pickle.dump(w,f)
    print(w) 

def wordLoadPik():
    with open('./quiz/pickle.pkl','rb') as f:
        w=pickle.load(f)
    print(w)   

def game():
    n=1
    q=random.choice(w)
    input('시작!')
    start = time.time()
    while n<=5:
        print("--{}번--".format(n))
        print(q)
        x=input()
        if q ==x:
            print("통과!")
            n=n+1
            q=random.choice(w)
        else:
            print("오타! 다시도전!")  
    end= time.time()
    print('걸린 시간 : {:.0f}초'.format(end-start))
    name = input('이름을 입력하세요')
    rank[name]=end-start
    print(rank)

def rankList():
    ranklist=sorted(rank.items(),key=(lambda x: x[1]))
    print(ranklist)
    cnt=1
    for k,v in ranklist:
        print('{}등 {} 시간:{:.2f}'.format(cnt,k,v)) 
        cnt+=1    

def endGame():
    with open('./quiz/rank.pkl','wb') as f:
         pickle.dump(rank,f)