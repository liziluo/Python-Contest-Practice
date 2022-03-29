sringa=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=int(input())
for y in range(n):
    h=[]
    h.append('A')
    m=int(input())
    z=list(map(int,input().split()))
    for i in range(m):
        if i%2==0:
            x=z[i]
            B=1
            for j in range(x):
                h.append(sringa[B])
                B+=1
            
        else:
            
            x=z[i]
            B=z[i]-1
            if ord(h[-1])<ord(sringa[z[i]]):
                h.pop(-1)
                h.append(sringa[z[i]])
         
                
            for k in range(x):
                h.append(sringa[B])
                B-=1
    print('Case #',y+1,':',' ',sep='',end='')
    for y in h:
        print(y,end='')
    print()
            
