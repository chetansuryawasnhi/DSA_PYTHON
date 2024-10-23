s="cdbcbbaaabab"
x=4
y=5
def fun(c,s,high,low,ad1,ad2):
            if high not in s and low not in s:
                return c
            
            elif high in s: 
                c+=s.count(high)*ad1
                s=s.replace(high,"")
                fun(c,s,high,low,ad1,ad2)
            elif low in s:
                c+=ad2   
                ind=(s.index(low))
                s=s[:ind]+s[ind+2:]
                fun(c,s,high,low,ad1,ad2)
c=0
ad1,high=(x,"ab") if x>=y else( y,"ba")
ad2,low =( y,"ba") if high=="ab" else (x,"ab")
if high in s or low in s:
            print(c)
            k=fun(c,s,high,low,ad1,ad2)
print(k)  