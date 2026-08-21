class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        lis=[1]*len(nums)

        for n in range(len(nums)):
            for i in range(n):
                if nums[i]<nums[n]:
                   lis[n]=max(lis[n],lis[i]+1)


        return max(lis)