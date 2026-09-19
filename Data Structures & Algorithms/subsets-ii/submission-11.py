class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        prevind=ind=0
        
        for i,n in enumerate(nums):
            if i>=1 and nums[i]==nums[i-1]:
                ind=prevind 
            else:
                ind=0
            
            prevind=len(res)
            for j in range(ind,prevind):
                tmp=res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res



            