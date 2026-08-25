class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elem={}

        for i,n in enumerate(nums):
            if n in elem:
                elem[n]+=1
            else:
                elem[n]=1
        
        top_k = sorted(elem, key=elem.get, reverse=True)[:k]
        return top_k
        