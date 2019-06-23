class Cookie:
    pass

a=Cookie()
b=Cookie()

print(type(a))
print(type(b))


class FourCal:
    
    def __init__(self,first=0,second=0):
        self.first=first
        self.second=second

    def setdata(self,first,second):
        self.first=first
        self.second=second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        return self.first/self.second

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second



c=FourCal(5,0)
d=SafeFourCal(5,0)
print(d.div())



class M:
    class_V = 0

a = M()
b = M()
print(a.class_V)
print(b.class_V)

M.class_V=5
print(a.class_V)
print(b.class_V)
a.class_V=6

print(a.class_V)
print(b.class_V)
