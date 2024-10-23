import 
word="alporfmdqsbhncwyu"
dre=Couter(word)
c=0
r=sorted(dre.values(),reverse=True)
print(r)
print(len(r))
print(dre)
k=1
so=2
ret = cycle = used = 0
for n in r:
            ret += (cycle+1)*n
            cycle += (used+1)//8
            used = (used+1)%8
print(ret)

print(c)
