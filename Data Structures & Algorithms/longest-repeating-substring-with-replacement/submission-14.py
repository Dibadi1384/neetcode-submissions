class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet=set(s)
        res=0

        for c in charSet:
            l,count=0,0
            for r in range(len(s)):
                #check how many we have of this char
                if s[r]==c:
                    count+=1
                #while there are more than k chars to replace
                while  ((r-l+1)-count)>k: 
                    #go from left to right and 
                    if s[l]==c: 
                        count-=1
                    l+=1

                res=max(res,r-l +1)
        return res
            