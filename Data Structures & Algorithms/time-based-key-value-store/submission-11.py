from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.TimeMap=defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.TimeMap:
            if timestamp in self.TimeMap[key]:
                return self.TimeMap[key][timestamp]
            else:
                prevtimestamp=timestamp
                while prevtimestamp not in self.TimeMap[key] and prevtimestamp>=0:
                    prevtimestamp-=1
                if prevtimestamp<0:
                    return ""
                return self.TimeMap[key][prevtimestamp]
        return ""
                
                
        
