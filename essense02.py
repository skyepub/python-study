la = []
la.append(10)
la.append(20)
print(la)
la.append(30)
print(la)

p = la.pop()
print(p)
print(la)

sum = 0
for i in range(0,10):
    sum = sum + i

print(sum)

k = 20

if k>30:
    print("30보다 큼")
    print("할말 없음")
else:
    print("30보다 작음")

k = 0
while k <10:
    print(k)
    k= k+1

print("while 끝남")

la = [5,2,3,4]
la.sort()
print(la)
la.reverse()
print(la)

def plus(v1, v2):
    ret = v1+v2
    return ret

calc = plus(200,300)
print(calc)


d1 = {'name':'허정윤',"age":20,"address":"부산시"}
print(d1)

ad = d1['address']
print(ad)

d1['age'] = 21
print(d1)

del(d1['name'])
print(d1)

# code for set 
# 집합연산 연습 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7}

sr1 = s1 & s2
print(sr1)

sr2 = s1 | s2
print(sr2)

sr3 = s1 - s2 
print(sr3)

sr4 = s1 ^ s2
print(sr4)







