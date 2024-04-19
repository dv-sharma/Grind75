class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0
        minnumber=float("inf")
        for price in prices:
            minnumber=min(price,minnumber)
            profit=price-minnumber
            maxprofit=max(maxprofit,profit)
        return maxprofit




