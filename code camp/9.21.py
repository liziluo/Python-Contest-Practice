path=0
size=int(input())
startPoint=list(input().split())
result=[]
path=0
def Golygon(x,y,path):
     if result and x==startPoint[0] and y==startPoint[1] :
         result.append((x,y))
         print(result)
         return 
     if x>=size or y>=size or x<0 or y<0 or (x,y) in result :
         return 
     result.append((x,y))
     x=x
     y=y
     path+=1
     Golygon(x,y+path,path)
     Golygon(x+path,y,path)
     Golygon(x,y-path,path)
     Golygon(x-path,y,path)
Golygon(startPoint[0],startPoint[1],path)
