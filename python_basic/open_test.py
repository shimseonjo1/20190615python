f=open("./python_basic/word.txt","r")

''' 쓰기(w)
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)    
'''
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()    