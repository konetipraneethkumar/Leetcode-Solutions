class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Brute force approach successful.
        '''max_profit = 0
        for buy in range(len(prices)):
            for sell in range(buy+1,len(prices)):
                profit =  prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit
            
            
        return max_profit'''
        # Optimized code 
        buy = 0 
        max_profit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            elif prices[i] < prices[buy]:
                buy = i
            else:
                profit = prices[i] - prices[buy]
                if max_profit < profit:
                    max_profit = profit
        return max_profit


        



prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))

