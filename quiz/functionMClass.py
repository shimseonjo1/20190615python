import random,time,pickle

class TypingGame:

    w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
    rank={}

    def rankLoad(self):
        with open('./quiz/rank.pkl','rb') as f:
            self.rank=pickle.load(f)

    def wordLoadTxt(self):
        f=open('./quiz/word.txt','r',encoding='utf8')
        lines=f.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].replace('\n','')
            self.w=self.w+lines 
        print(self.w)
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

    def wordSaveTxt(self):
        f=open('./quiz/word.txt','w',encoding='utf8')
        for i in self.w:
            data=''
            data+=i+'\n'
            f.write(data)
        f.close()

    def wordAppend(self):
        quiz=1
        while quiz:
            quiz=input('추가할 단어 입력(종료:0) >> ')
            if quiz=='0':
                print('입력을 종료합니다.')
                break
            self.w.append(quiz)
        print(self.w)

    def wordSavePik(self):
        with open('./quiz/pickle.pkl','wb') as f:
            pickle.dump(self.w,f)
        print(self.w) 

    def wordLoadPik(self):
        with open('./quiz/pickle.pkl','rb') as f:
            self.w=pickle.load(f)
        print(self.w)   

    def game(self):
        n=1
        q=random.choice(self.w)
        input('시작!')
        start = time.time()
        while n<=5:
            print("--{}번--".format(n))
            print(q)
            x=input()
            if q ==x:
                print("통과!")
                n=n+1
                q=random.choice(self.w)
            else:
                print("오타! 다시도전!")  
        end= time.time()
        print('걸린 시간 : {:.0f}초'.format(end-start))
        name = input('이름을 입력하세요')
        self.rank[name]=end-start
        print(self.rank)

    def rankList(self):
        ranklist=sorted(self.rank.items(),key=(lambda x: x[1]))
        print(ranklist)
        cnt=1
        for k,v in ranklist:
            print('{}등 {} 시간:{:.2f}'.format(cnt,k,v)) 
            cnt+=1    

    def endGame(self):
        with open('./quiz/rank.pkl','wb') as f:
            pickle.dump(self.rank,f)

    def menuDisplay(self):
        print('''
        1.문제불러오기 
        2.문제txt저장하기
        3.문제추가 
        4.문제 피클로 저장 
        5.피클 문제 읽기
        6.타자게임 
        7.등수리스트 
        8.종료하기''')
        menu = input("메뉴를 선택하세요 >> ")
        return menu

    def exe(self,menu):
        if menu=='1':
            self.wordLoadTxt()
        elif menu=='2':
            self.wordSaveTxt()
        elif menu=='3':
            self.wordAppend()
        elif menu=='4':
            self.wordSavePik() 
        elif menu=='5':
            self.wordLoadPik()
        elif menu=='6':
            self.game()      
        elif menu=='7':
            self.rankList()
        elif menu=='8':
            self.endGame()
  
    def __init__(self):
        self.rankLoad()
        while True:
            self.exe(self.menuDisplay())