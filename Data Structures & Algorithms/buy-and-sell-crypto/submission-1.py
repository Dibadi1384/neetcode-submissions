class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        for i,buy in enumerate(prices):
            for j in range(i+1,len(prices)):
                sell=prices[j]
                maxprof=max(maxprof, sell-buy)

        return maxprof

        