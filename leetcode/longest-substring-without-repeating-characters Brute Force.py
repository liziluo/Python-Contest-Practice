a=list(input())
counter=1
num=len(a)
for i in range(num):
    sum1=[]
    sum1.append(a[i])
    for j in range(i+1,num):
        if a[j] in sum1:
            break
        else:
            sum1.append(a[j])
        temp=len(sum1)
        if temp>counter:
            counter=temp
print(counter)
##Brute Force
##class Solution:
##    def lengthOfLongestSubstring(self, s: str) -> int:
##        counter=1
##        if not s:return 0
##        num=len(s)
##        for i in range(num):
##            sum1=[]
##            sum1.append(s[i])
##            for j in range(i+1,num):
##                if s[j] in sum1:
##                    break
##                else:
##                    sum1.append(s[j])
##                temp=len(sum1)
##                if temp>counter:
##                    counter=temp
##        return(counter)

