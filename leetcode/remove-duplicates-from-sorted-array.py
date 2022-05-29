##nums=list(map(int,input().split()))
##num1=len(nums)
##a=0
##for i in range(num1):
##    a=nums.count(nums[i])-1
##    while a!=0:
##        nums.pop(i)
##        a-=1
##
##print(nums)

nums=list(map(int,input().split()))
num1=len(nums)
fast=low=0
while fast<num1:
    for i in range(num1):
        if fast[i]==fast[i-1]:
            fast+=1
        else:
            
    


