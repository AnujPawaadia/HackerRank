inp1=input()
eng=list(map(int, input().split()))
eng.sort()
inp2=input()
fre=list(map(int, input().split()))
fre.sort()

p1=0
p2=0
c=0
while p1<len(eng) and p2<len(fre):
    if eng[p1]==fre[p2]:
        p1=p1+1
        p2=p2+1
        c=c+1
    elif eng[p1]<fre[p2]:
        p1=p1+1
    else:
        p2=p2+1
                
        
print((len(eng)-c)+(len(fre)-c))
