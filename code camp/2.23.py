from math import sqrt
global current
current=[]
x="numbers-1.txt"
with open(x) as f:
    for line in f:
        for word in line.split():
            current.append(int(word))

def que1():
    result=0
    for i in current:
        if i%2==1:
            result+=i
    print(result)

def que2():
    result=0
    for i in current:
        i=str(i)
        d = i[::-1]
        if d==i:
            result+=1
    print(result)


def isPrimes1(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
  
def que3():
    result=0
    for i in current:
        if isPrimes1(i):
            result+=1
    print(result)

def que4():
    range1=9999999999
    x=[]
    for i in range(len(current)):
        for j in range(i+249,len(current)):
            x=current[i:j]
            currentresult=max(x)-min(x)
            if currentresult<range1:
                range1=currentresult
    print(range1)

def que5():
    number=0
    for i in current:
        index1=current.index(i)
        if current[index1]>current[index1+1]:
            current.pop(index1)
            number+=1

que1()
que2()
que3()
que4()

            
            
    
    
    
