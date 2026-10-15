from sortedcontainers import SortedDict

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        endtimes={}
        starttimes=SortedDict()
        res=[]

        for interval in intervals:
            start,end=interval[0], interval[1]
            if end in endtimes:
                endtimes[end]=min(start,endtimes[end])
            else:
                endtimes[end]=start

        for end in endtimes:
            start=endtimes[end]
            if start in starttimes:
                starttimes[start]=max(end,starttimes[start])
            else:
                starttimes[start]=end
        print(endtimes, starttimes)

        prevend=-1
        prevstart=-1

        for start in starttimes:
            end=starttimes[start]
            newend=end
            newstart=start
            if start<=prevend:
                newend=max(end, starttimes[prevstart])
                starttimes[prevstart]=newend
                newstart=prevstart
                starttimes[start]=-1

            prevend=newend
            prevstart=newstart
            
        for start in starttimes:
            if starttimes[start]!=-1:
                res.append([start,starttimes[start]])
        return res
    
    
    

    