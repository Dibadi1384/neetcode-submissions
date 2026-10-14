class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]

        for i,num in enumerate(nums):
            other=target-num
            d[other]=i

        for j,other in enumerate(nums):
            
            if other in d and not res:
                if d[other]==j:
                    continue
                res.append(j)
                res.append(d[other])

        return res



            