a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=list(map(int,input().split()))
    sum1=sum(d)
    num=sum1%c
    print("Case #%d: %d"%(i+1,num))

    
