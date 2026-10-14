class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        ls=0
        l=0

        for r in range(len(s)):
            if s[r] in mp:
                l=max(l,mp[s[r]]+1)

            mp[s[r]]=r
            ls=max(ls, r-l +1)
        return ls


            



        