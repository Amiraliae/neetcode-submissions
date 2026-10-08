class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if(prices[i]-minn>ans):
                ans= prices[i] - minn
            if(prices[i]<minn):
                minn  = prices[i]
        return ans
        