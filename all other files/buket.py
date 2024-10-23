fruits=[0,1,6,6,4,4,6]
c=0
m=0
i=0
j=0
k =0
while k <len(fruits):
    if fruits[i]==fruits[k ] or fruits[j]==fruits[k ]:
        c+=1
        if fruits[j]!=fruits[k ]:
            i=j
            j=k 
            
        k +=1
    elif i==j:
        j=k 
        c+=1
        k +=1
    else:
        i=j  
        j=k 
        m=max(c,m)
        c=j-i+1
        k+=1
m=max(m,c)
print(m)