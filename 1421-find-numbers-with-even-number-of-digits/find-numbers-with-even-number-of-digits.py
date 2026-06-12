class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #approach 1
        """
         even_dig_count = 0
        for i in range(len(nums)):
            dig_count = 0
            num = nums[i]
            while num != 0:
                num = num // 10
                dig_count+=1
            if dig_count %2 ==0:
                even_dig_count +=1
        return even_dig_count
        """
        #approach 2
        """
        even_dig_count = 0
        for i in range(len(nums)):
            dig_count = 0
            while nums[i] != 0:
                nums[i] = nums[i] // 10
                dig_count+=1
            if dig_count %2 ==0:
                even_dig_count +=1
        return even_dig_count"""
        #approach 3
        count = 0
        for i in nums:
            digits = len(str(i))
            if digits %2 ==0:
                count+=1
        return count
sol = Solution()
nums = [555,901,482,1771]
print(sol.findNumbers(nums))
