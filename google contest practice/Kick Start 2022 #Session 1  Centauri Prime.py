a=int(input())
v=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in range(a):
    f=""
    nam=str(input())
    nam2=list(nam)
    
    if nam2[-1]=="y" or nam2[-1]=="Y":
        f="nobody"
    elif(nam2[-1] in v):
            
        f="Alice"
    else:
        f="Bob"

    print("Case #%d: %s is ruled by %s."%(i+1,nam,f))

    
