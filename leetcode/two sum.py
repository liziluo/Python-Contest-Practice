num3=list(map(int,input().split()))
target=int(input())
double=[]
flag=0
if target%2==0:
    half=target//2
    if half  in num3:    
        for i in range(len(num3)):
            if num3[i]==half:
                double.append(i)
            if len(double)==2:
                print("[%d,%d]" %(double[0],double[1]))
                flag=1
                break
                
        
if flag==0:      
    for i in range(len(num3)):
        num1=target-num3[i]
        if num1 != num3[i]:
            if num1 in num3:
                print("[%d,%d]" %(i,num3.index(num1)))
                break

    
