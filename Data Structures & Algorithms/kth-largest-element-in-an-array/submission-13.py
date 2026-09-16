class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]

        #heapq.heappush(heap, nums[0])
        for i, num in enumerate(nums):
            if len(heap)==k:
                if num>heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
            #print(num,heap)
      
        return heapq.heappop(heap)
                    
                
        