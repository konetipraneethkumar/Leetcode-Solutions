class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hmap = {}        
        for val in nums:
            hmap[val] = hmap.get(val,0)+1
            if hmap[val] > len(nums)//2:
                return val
        return