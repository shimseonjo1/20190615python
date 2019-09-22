import urllib.request

request=urllib.request.Request("http://www.naver.com")
response=urllib.request.urlopen(request)
print(response.read().decode())
print(request.get_method())
request.method='POST'
print(request.get_method())
print(request.type)
print(request.host)