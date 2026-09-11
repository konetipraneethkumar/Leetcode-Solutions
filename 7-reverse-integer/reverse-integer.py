class Solution:
    def reverse(self, x: int) -> int:
        
        num = abs(x)
        temp = 0
        while num>0:
            dig = num % 10
            temp = temp * 10 + dig
            num = num // 10
        if x < 0:
            temp =  temp * (-1 )
        if temp < (-2) ** 31 or temp > (2 ** 31)-1:
            return 0
        return temp