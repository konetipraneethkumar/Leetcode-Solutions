class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest_cust =0
        sum = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[0])):
                sum =sum + accounts[i][j]
                if sum > richest_cust:
                    richest_cust = sum
            sum = 0
        return richest_cust
        