##input1=[]
##while True:
##    n= input())
##    if n == '':
##    	break
##    input1.append(int(n))
##    
##
##n=input1[0]
n=2868
number=0
for i in range(1,n):
    if ((i+1)*i)/2<n:
        number=i
    else:
        number=i
        if (((i+1)*i)/2-n)%2==0:
            number+=1
        break

    

maxpage=(number+1)*number/2
lostpage=maxpage-n
currentpage=lostpage
result=[]
for i in range(2*number): #if just one page lost
    if currentpage==i+i-1:
        print(n,number,i,i-1)
        
result=[[0]*(lostpage+1) for i in range(number+1)]
for i in range(number+1):
    for j in range(lostpage+1):
        if 2*i-1==j:
            result[i][j].append(i)
        if j-2*i-1>0 and result[i][j-2*i-1]!=0:
            result[i][j]=result[i][j-2*i-1]
            result[i][j].append(i)
print(result[i][j])

