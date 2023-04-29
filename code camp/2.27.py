pi=3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989

pi=str(pi)
result=[]
global flag
flag=0
sblist=[]
def findstring(n):
    x=0
    global flag
    if n:
        number=0
        n=str(n)
    else:
        flag=1
        return 0
    for i in range (len(n)):
        if flag!=0:
           break
        if number!=0 and x and x!=len(n):
            sblist.append(n[:x-1])
            z=n[x-1:]
            findstring(z)
        for j in range (len(pi)):
            if n[i]==pi[j] and number==0:            
                result.append(j)
                number=j
                while(1):
                     if n[i]!=pi[j]:
                         break
                     else:
                         i=i+1
                         j=j+1
                         x=i
                     if i==len(n) or j==len(pi):
                         flag=1
                         sblist.append(n)
                         break
            if number!=0:
                break

n=897932384159
m=415926
x=9999999999999
inpu1=int(input())
findstring(n)

output=len(result)
if output==1:
    print("1 sequence: index %d (%s)" %(result[0],n))
if output==2:
    print("2 sequence: index %d (%s) and index %d (%s)" %(result[0],sblist[0],result[1],sblist[1]))
if output==3:
    print("3 sequence: index %d (%s) and index %d (%s and index %d (%s))" %(result[0],sblist[0],result[1],sblist[1],result[2],sblist[2]))
if output>=3:
    print("(I'll leave finding one of the many ways you can do it in 3 sequences to you)")



