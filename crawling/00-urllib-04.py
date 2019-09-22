import urllib.parse

parameter = {'key1' : 'value1', 'key2' : 'value2 test'}
 
data1 = urllib.parse.urlencode(parameter, quote_via=urllib.parse.quote)
data2 = urllib.parse.urlencode(parameter)
 
print(data1)
print(data2)


parameter = {'key1' : 'value1', 'key2' : ['value2', 'value3']}
 
data1 = urllib.parse.urlencode(parameter)
data2 = urllib.parse.urlencode(parameter, doseq=True)
 
print(data1)
print(data2)
