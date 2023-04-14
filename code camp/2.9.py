from itertools import combinations
from itertools import permutations

deck = ["2C","2D","2H","2S","3C","3D","3H","3S","4C","4D","4H","4S","5C","5D","5H","5S","6C","6D","6H","6S","7C","7D","7H","7S","8C", "8D","8H","8S","9C","9D","9H","9S","TC","TD","TH","TS","JC", "JD","JH","JS","QC","QD","QH","QS","KC","KD","KH","KS","AC", "AD", "AH", "AS"]

def number(x):
    for i in  range(len(deck)):
        if deck[i]==x:
            return i

def Mike (n,m):
    z,o=[],[]
    for i in n:
        x=number(i)
        z.append(x)
    z.sort()
    for p in permutations(z):
        o.append(list(p))
    if i in range(len(o)):
        prints(z[i])
        
    

    


n=list(input().split())
print(number(n[0]))
m=0
for i in n:
    x=n.copy()
    x.remove(i)
    number1=number(i)
    Mike(x,number1)
