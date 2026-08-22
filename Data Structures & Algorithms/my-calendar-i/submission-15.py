class MyCalendar:
    
    def __init__(self):
        
        self.time=[]

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(len(self.time)):
            if self.time[i][0]<startTime<self.time[i][1] or self.time[i][0]<endTime<=self.time[i][1]:
                return False
            if startTime<self.time[i][1] and endTime>self.time[i][1]:
                return False
        

        self.time.append([startTime,endTime])
        return True
         


      


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)