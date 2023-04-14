acount=0
result=[]


import datetime

today = datetime.datetime.today()
oneday = datetime.timedelta(days=1)

while True:
    left = "%s" % today.year
    right = "%02d%02d" % (today.month, today.day)
    if left == right[::-1]:
        result1=left+right
        result1=int(result1)
        result.append(result1)
        acount+=1
    today = today + oneday
    if acount==132:
        break

print(result)

average=[]
##
##
##    
##for x in range(0,100000):
##    x=str(x)
##    if x==x[::-1]:
##        acount+=1
##    else:
##        continue
##    if acount==121:
##        result=x
##        break
##result=float(result)/365
##print("%.2f" %result)
##    
