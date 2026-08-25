class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res=nums[0]
        minv,maxv=1,1

        for num in nums:
            temp=maxv*num

            maxv=max(temp, minv*num, num)
            minv=min(temp, minv*num, num)      


            res=max(res,maxv)  

        return res
        