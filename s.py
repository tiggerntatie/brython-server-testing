from a import A
        
class S(object):
    def __init__(self):
        A.x.append(len(A.x))
        

if __name__ == '__main__':
  s1 = S()
  s2 = S()
  s3 = S()
  a = A()
