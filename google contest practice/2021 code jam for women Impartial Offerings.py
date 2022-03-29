n=int(input())
for i in range(n):
    count=0
    temp=0
    count2=0
    
    m=int(input())
    z=list(map(int,input().split()))
    z.sort()
    for j in range(m):
        if temp==z[j]:
            count+=count2
        elif z[j]>temp:
            temp=z[j]
            count2+=1
            count+=count2
    print('Case #',i+1,':',' ',count,sep='')
