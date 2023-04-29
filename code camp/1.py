n=[25,10,5,1]
five=[1,2,3,2,1]
result=0
z=29
z=int(input("coin:"))
for i in range( len(n)):
    if z==0:
      break
    if (z<=5 and z>0) or(z<0 and z>=-5 ):
        result+=1
        break
    while z>0 and z-i>=0:
        result+=1
        z-=n[i]
    if abs(z-i)<z:
        result+=1
        z-=n[i]
        continue
    else:
        continue
    
    while z<0 :
        result+=1
        z+=n[i]
    if abs(z)<z+i:
        z-=0
        result-=1
        z+=n[i]

print(result)
        
    
    
        
        
        

        
