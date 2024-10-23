happiness = [1,1,1,1]
k=1
k1=[]
for i in range(k):
    k1.append(happiness.pop())
k1.sort(reverse=True)
for j in range(len(k1)):
    k1[j]=k1[j]-j
print(sum(k1))