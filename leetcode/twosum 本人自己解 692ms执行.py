class Solution:##此题解15.6M内存
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        double=[]
        flag=0
        if target%2==0:
            half=target//2
            if half  in nums:    
                for i in range(len(nums)):
                    if nums[i]==half:
                        double.append(i)
                    if len(double)==2:
                        flag=1
                        return[double[0],double[1]]
                    
        
        if flag==0:      
            for i in range(len(nums)):
                num1=target-nums[i]
                if num1 != nums[i]:
                    if num1 in nums:
                        return[i,nums.index(num1)]


###用时720方法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag=0
        if target%2==0:
            half=target//2
            if nums.count(half)==2:
                x=nums.index(half)
                y=nums.index(half,x+1)
                flag=1
                return[x,y]
                    
        
        if flag==0:      
            for i in range(len(nums)):
                num1=target-nums[i]
                if num1 != nums[i]:
                    if num1 in nums:
                        return[i,nums.index(num1)]
                
