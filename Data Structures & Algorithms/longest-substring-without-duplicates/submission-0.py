class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        mp={}
        l=0
        res=0

        for r in range(len(s)):
            if s[r] in mp:
                #we do the max,1 so if the index of repeating char is outside window it wont count
                l=max(mp[s[r]]+1, l)
            mp[s[r]]=r #update the index for that char
            res=max(res, r-l+1)
        return res