print("Hello from https://github.com/tiggerntatie/brython-server-testing")

class t(object):
    def __init__(self):
        self.x = 1
        
class u(t):
    
    def sety(self, y = self.x):
        self.y = y

uinst = u()
print(uinst.y)