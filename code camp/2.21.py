from itertools import combinations
globalcurrentbook=[]
x="wordlist.txt"
with open(x) as f:
    for line in f:
        for word in line.split():
            currentbook.append(word)

def qu1():
    result=[]
    c = ('t','e','r','g','a')
    for j in combinations(c,5):
        str1=''.join(j)
        if str1 in currentbook:
            result.append(str1)
    for x in range(0,5):
        for j in combinations(c,x):
            for z in combinations(j,x):
                str1=''.join(z)
                if str1 in currentbook:
                    result.append(str1)

    print(len(result))
    


def qu2():
    flag=0
    qu1=["u","a","e","o","c"]
    qu4='aeouc'
    quo='qith'
    qu2=["q","i","t","h"]
    result=currentbook
    for x in qu1:
        for j in result:
            if x in j:
                continue
            else:
                result.remove(j)
                
    print(len(result))

def qu3():
    z=("n","m","o")
    result=[]
    list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in list1:
        newlist=list(z)
        newlist.append(i)
        newlist=tuple(newlist)
        for x in range(0,4):
            for j in combinations(newlist,x):
                for z in combinations(j,x):
                    str1=''.join(z)
                    if str1 in currentbook and str1 not in result:
                        result.append(str1)
    print(len(result))
        
def qu4():
    result=[]
    c = 'qrgy'
    letter=[]
    for j in combinations(c,4):
        str1=''.join(j)
        if str1 in currentbook:
            result.append(str1)
        
    for x in range(0,5):
        for j in combinations(c,x):
            for z in combinations(j,x):
                str1=''.join(z)
                if str1 in currentbook:
                    result.append(str1)
            


qu3()
qu1()
qu2()
