import urllib.request
response=urllib.request.urlopen("http://www.naver.com")

print(response.geturl())

print(response.getcode())

#헤더의 정보
print(response.info())

#print( response.read())
print( response.read().decode())
