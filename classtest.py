class t0(object):
    def __init__(self):
        self.zz = top


class t1(t0):
    def __init__(self):
        self.x = 5
        self.z = q
        
class t2(t1):
    def __init__(self):
        super().__init__()
        self.y = 6
        
t = t2()

print(t.x)
print(t.y)
print(t.zz)
