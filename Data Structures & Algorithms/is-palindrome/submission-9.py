class Solution:
    def isPalindrome(self, s: str) -> bool:
        heapmin=[]
        heapmax=[]

        for i, letter in enumerate(s):
            if letter.isalpha() or letter.isalnum():
                if letter.isalpha():
                    letter=letter.lower()
            
                heapq.heappush(heapmin, (i, letter))
                heapq.heappush(heapmax, (-i, letter))
                
        
        while heapmin and heapmax:
            _, l=heapq.heappop(heapmin)
            _, r=heapq.heappop(heapmax)
            if l!=r:
               return False
        
        return True
                
        
        

        
        