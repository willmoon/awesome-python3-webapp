def fab_1(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        n += 1
        a,b = b,a + b

def fab_2(max):
    _list = [ ]
    n , a, b = 0, 0, 1
    while n < max:
        _list.append(b)
        n += 1
        a, b = b, a + b
    return _list

#fab_1(5)

class fab_3(object):

    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b ,self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

#for n in fab_3(5):
#    print(n)
f = fab_3(5)

print(f.next())

def fab_4(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

for n in fab_4(5):
    print(n)
