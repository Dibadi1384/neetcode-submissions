class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxprof=0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maxprof=max(maxprof, prices[j]-prices[i])
        # return maxprof

        # l,r =0,1
        # maxp=0

        # while r < len(prices):
        #     if prices[r]>prices[l]:
        #         prof=prices[r]-prices[l]
        #         maxp=max(prof,maxp)
        #     else:
        #         l=r
        #     r+=1
        # return maxp

        maxP=0
        minBuy=prices[0]
        for sell in prices:
            minBuy=min(minBuy,sell)
            maxP=max(maxP, sell-minBuy)
        return maxP
               
