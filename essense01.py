# 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

from importlib.abc import ResourceLoader
from pickle import PickleBuffer
from select import POLLRDHUP


def plus(v1,v2):
    res = 0
    res = v1+v2
    return res



a = 200
message = ""
if a>100:
    message = "Big Number"
elif a>50:
    message = "Moderate"
else:
    message = "Small Number"

print(message)


for i in range(0,5):
    print(i," ",end=" ")

print(' ')


a = 23
b = 43
c = plus(a,b)
print(c)

# list 
aa = []
aa.append(0)
aa.append(1)
aa.append(2)

for i in range(3,10):
    aa.append(i)

print(aa)

print(aa[4:7])

aa.insert(1,10000)
print(aa)

aa.sort()
print(aa)

aa.reverse()
print(aa)

aa.reverse()
print(aa)

def twotimes(v):
    return v*2

ab = list(map(twotimes,aa))
print(ab)


# dictionary 
info = {}
info['name'] = "Jiung"
info['language']="korean"
info['city']="busan"
info['secret']='secret_12kdk3kd'

print(info['name'])
print(info)

del(info['secret'])
print(info)

info['name'] = "Jiung Heo"
print(info)

print(info['language'])
print(info.get('language'))

keys = info.keys()
print(keys)
values = info.values()
print(values)

for k in keys:
    print(k)

for v in values:
    print(v)

# set
sa = {1,2,3,4,5,6}
sb = {4,5,6,7,8}

print(sa)
print(sb)

sr1 = sa & sb
sr2 = sa | sb
sr3 = sa - sb
sr4 = sa ^ sb

print(sr1)
print(sr2)
print(sr3)
print(sr4)

sr1 = sa.intersection(sb)
sr2 = sa.union(sb)
sr2 = sa.difference(sb)
sr2 = sa.symmetric_difference(sb)

print(sr1)
print(sr2)
print(sr3)
print(sr4)

# tuple
tt1 = (10,20,30)
print(tt1)

tt2 = 10,20,30
print(tt2)

# 항목이 하나인 경우 ,를 붙여서 튜플임을 표시
tt3 = 10,
tt4 = (20,)

print(tt1[2])
print(tt2[1])

# 튜플은 내부의 값을 바꿀수는 없으나 간단한 연산 결과는 돌려줄 수 있다. 
tta = ('a','b')
ttb = ('c','c')

tr1 = tta + ttb
print(tr1)

tr2 = tr1 * 3
print(tr2)


# list, tuple 상호변혼
la = list(tta)
print(la)
la.append('k')
print(la)
tca = tuple(la)
print(tca)


# 문자열
str1 = "we are the world"
str2 = "we are the children."
strb = str1[3:6]
print(strb)
strb = str1[7:]
print(strb)

stra = str1 + ", " + str2
print(stra)
strc = str1 * 3
print(strc)

print(len(str1))

countFound = stra.count('we')
print(countFound) 

# find는 찾은 위치를 돌려줌 , 못찾으면 -1을 돌려줌
pos1 = stra.find("the")
print(pos1)

pos2 = stra.rfind("the")
print(pos2)

# index는 없을 경우 오류발생
index1 = stra.index("the")
print(index1)

index2 = stra.rindex("the")
print(index2)

# startswith, endswith
r1 = str1.startswith("we")
print(r1)

r2 = str2.endswith("children.")
print(r2)

# split
strd = "python is powerful language."
sr5 = strd.split()
print(sr5)
strd = "python:is:powerful:language."
str5 = strd.split(':')
print(str5)


















