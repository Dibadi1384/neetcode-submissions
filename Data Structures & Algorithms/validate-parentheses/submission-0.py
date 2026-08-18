class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen = {")":"(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                   stack.pop()
                else:
                    return False #closing with no openinh
            else:
                stack.append(c)
        
        if not stack: #opening with no closing
            return True
        else:
            return False
