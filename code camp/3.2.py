n="KLMABCDXYZ"
m=1
##list1=['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O
##       , ‘P’, ‘Q’, ‘R’, ‘S’, ‘T’, ‘U’, ‘V’, ‘W’, ‘X’, ‘Y’, 'Z']

arr="CBDHDE"
alphabet = "ABCDEFGHIJKLMNOPQRSTUV"
list1=[]
current=0  #flag
max1=0
for i in range(len(arr)):
    if i<max1:
        continue
    current=i
    for j in range(len(alphabet)):
        current=i
        x=i
        y=j
        if arr[x]!=alphabet[y]:
            continue
        while (arr[x]==alphabet[y]):
            max1=x
            x+=1
            y+=1
            if x==len(arr) or y==len(alphabet):
                list1.append(arr[current:])
            print(arr[x])
        list1.append(arr[current:max1])
        print(arr[current:max1])
        break

print(list1)


                
                
        
