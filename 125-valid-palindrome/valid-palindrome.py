class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        cleaned = ""
        if  s == " ":
            return True
        for i in s:
            if 'a' <= i <= 'z':
                cleaned +=i
            elif('0'<=i<='9'):
                cleaned +=i
        if ( cleaned == cleaned[::-1]):
            return True
        else:
            return False
s = "race a car"
sol = Solution()
print(sol.isPalindrome(s))