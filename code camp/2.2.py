n=int(input())
input1=[]
while n>0:
    a=list(input().split())
    for i in range (len(a)):
        if a[i]=='false':
            a[i]=0
        if a[i]=="true":
            a[i]=1

    input1.append(a)
    n=n-1

def check(z):
    z1=z[0:3]
    z2=z[3:]
    while  len(z)>1:
        if z1==[0,"and",1] or z1==[0,"and",0] or z1==[1,'and',0] or z1==[0,'or',0] or z1==[1,'xor',1] or z1==[0,'xor',0] :
            z2.insert(0,0)
        elif z1==[1,'and',1] or z1==[1,'or',0] or z1==[0,'or',1] or z1==[1,'or',1] or z1==[1,'xor',0]or z1==[0,'xor',1]:
            z2.insert(0,1)
        z=z2
        print(z)
        z1=[]
        if len(z)>=3:
            z1=z[0:3]
            z2=z[3:]
        else:
            return z[0]

    
result2=[]
true1=0
false1=0
for a in input1:
    result=[0,0]
    if len(a)==1 and a[0]==1:
        result2.append([0,1])
        continue;
    elif len(a)==1 and a[0]==0:
        result2.append([1,0])
    if len(a)==3:
        result1=check(a)
        if result1:
            result[1]+=1
        else:
            result[0]+=1
        result2.append(result)
        continue

    for i in range(len(a)):
        for j in range(len(a)):
            if isinstance(a[i],int) and isinstance(a[j],int):
                a1=a[0:i]
                a2=a[i:j+1]
                a3=a[j+1:]
                if not a1 and not a3:
                    continue
                x=check(a2)
                print(a1)
                a1.append(x)
                a1=a1+a3
                print(a1)
                result1=check(a1)
                if len(a1)==1:
                    result1=a1
                if result1:
                    result[1]+=1
                else:
                    result[0]+=1
    result2.append(result)

        
for i in result2:
    print("%d true and %d false" %(i[1],i[0]))
