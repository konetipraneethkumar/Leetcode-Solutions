class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ha = {}
        for num in nums:
            ha[num] = ha.get(num,0) +1
        for num, fre in ha.items():
            if fre < 2 or fre > 2:
                return num
        

        