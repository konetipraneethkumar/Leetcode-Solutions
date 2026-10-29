class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """ 
        hmap = {}        
        for val in nums:
            hmap[val] = hmap.get(val,0)+1
            if hmap[val] > len(nums)//2:
                return val
        return
        """
        candidate = None
        count = 0

        for val in nums:
            if count == 0:
                candidate = val

            if val == candidate:
                count += 1
            else:
                count -= 1

        return candidate