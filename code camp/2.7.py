n=str(input())
m=str(input())
result=[[" " for i in range(4)]for _ in range(4)]
number=0
print(len(n))
for i in range(len(n)):
    x=i//4
    y=i%4
    result[x][y]=n[i]
print(result)
stencil1=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
stencil2=[[12,8,4,0],[13,9,5,1,],[14,10,6,2],[15,11,7,3]]
stencil3=[[15,14,13,12],[11,10,9,8],[7,6,5,4],[15,11,7,3]]
stencil4=[[3,7,11,15],[11,10,9,8],[7,6,5,4],[3,2,1,0]]

ans1=[]

for i in range(4):
    for j in range(16):
        x=j//4
        y=j%4
        if m[i]==" ":
            continue
        if result[x][y]==(m[i]) and [x,y] not in ans1:
            ans1.append([x,y])
            break
print(ans1)
ans2=[]
ans3=[]
ans4=[]
ans5=[]
for i in ans1:
    a,b=i
    ans2.append(stencil1[a][b])
    ans3.append(stencil2[a][b])
    ans4.append(stencil3[a][b])
    ans5.append(stencil4[a][b])
print(ans2,ans3,ans5,ans4)
