class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        l = 0
        r = 1
        for index,price in enumerate(prices):
            print(index)
            if r > len(prices) - 1:
                break

            if (prices[l] > prices[r]):
                l=r
                r+=1
            else:
                profit = prices[r] - prices[l]
                if max_profit < profit:
                    max_profit =profit 
                r+=1
            
        return max_profit


        