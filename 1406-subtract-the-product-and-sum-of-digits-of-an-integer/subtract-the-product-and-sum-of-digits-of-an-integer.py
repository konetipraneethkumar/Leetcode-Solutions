class Solution(object):
    def subtractProductAndSum(self, num):
        """
        :type n: int
        :rtype: int
        """
        dig_sum = 0 
        dig_prod = 1
        
        while num > 0:
            dig = num % 10
            num = num //10
            dig_sum += dig
            dig_prod *= dig
        res = dig_prod - dig_sum
        return res 




        