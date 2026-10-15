class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        numbermap={}
        res=[]
        prod=1
        prod2=1

        for i, num in enumerate(nums):
            numbermap[i]=prod
            prod*=num

        for i in range(len(nums)-1, -1, -1):
            numbermap[i]*=prod2
            prod2*=nums[i]
        
        for number in numbermap:
            res.append(numbermap[number])
        return res

        

        

       
        