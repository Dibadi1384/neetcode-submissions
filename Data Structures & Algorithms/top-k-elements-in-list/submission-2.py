class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        h=[]
        res=[]


        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1

        for num in d:
            heapq.heappush(h, (-d[num], num))

        while k>0:
            k-=1
            _, num=heapq.heappop(h)
            res.append(num)
        
        return res

            
