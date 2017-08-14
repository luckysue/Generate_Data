# coding:utf-8

X = []
Y = []
for i in range(26):
    X.append(i+1)
    Y.append(chr(97+i))
print(X)
print(Y)

def get_index(m):
    n = []
    for i in m:
        n.append(Y.index(i)+1)
    print(n)

def get_letters(n):
    L = []
    for i in n:
        L.append(Y[i])
    print(L)

get_index('aaaa')
get_index('bdzb')
get_index('cgac')
get_index('djzd')
get_letters([4,12,0,4])

get_index('didiidid')
get_index('diidiidd')


