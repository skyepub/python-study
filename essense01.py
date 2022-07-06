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

aa = []
aa.append(0)
aa.append(1)
aa.append(2)

for i in range(3,10):
    aa.append(i)

print(aa)


