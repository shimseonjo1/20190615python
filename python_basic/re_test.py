import re

p = re.compile('[a-z]+')

m =  p.finditer("as3 pythOn")
print(m)
for r in m:
    print(r)
