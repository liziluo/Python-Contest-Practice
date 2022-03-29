
a=int(input())
for i in range(a):
    acc=1
    c=int(input())
    d=list(map(int,input().split()))
    list1=[0]*c
    for j in range(c):
        acc1=0
        for z in range(j+1):
            tem=acc+1
            if d[z]>=tem:
                acc1+=1
            if tem==acc1:
                acc+=1
                
        list1[j]=acc
    
    print("Case #%d:"%(i+1),end=" ")
    for i in list1:
        print(i,end=" ")
    print()
                
            
            
            
            
    

            
    
