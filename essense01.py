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