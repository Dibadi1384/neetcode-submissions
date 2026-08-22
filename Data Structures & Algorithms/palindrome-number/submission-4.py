class Solution:
    def isPalindrome(self, x: int) -> bool:
        number=collections.deque()
        while (x>=10):
            number.append(x%10)
            x=x//10
        number.append(x)

        while len(number)>=2:
            if number[0]==number[-1]:
                number.pop()
                number.popleft()
            else:
                return False
            
        if len(number)==0 or (len(number)==1 and number[0]>=0):
            return True
        else:
            return False


        