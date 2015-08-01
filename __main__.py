print("Hello from https://github.com/tiggerntatie/brython-server-testing")

x = [1,2,3,4,5,6]
f = lambda x : x % 2 == 0
y = filter(f, x)
print(list(y))
print(x)