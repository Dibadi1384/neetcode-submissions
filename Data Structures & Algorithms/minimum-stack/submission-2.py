from collections import deque

class MinStack:

    def __init__(self):

        self.stack=deque()
        self.minstack=deque()
           

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            minnum=self.minstack[-1]
            if val<minnum:
                self.minstack.append(val)
            else:
                self.minstack.append(minnum)
                
        else:
            self.minstack.append(val)
        return 
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        return
        

    def top(self) -> int:
        return self.stack[-1] 
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
