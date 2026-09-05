class Solution(object):
    def isPalindrome(self, x):
        num = x
        """
        :type x: int
        :rtype: bool
        """
        temp = num
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev *10 + dig
            num = num //10
        if temp == rev:
            return True
        return False
            
            

            

        