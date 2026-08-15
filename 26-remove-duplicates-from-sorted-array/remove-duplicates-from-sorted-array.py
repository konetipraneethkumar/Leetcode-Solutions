class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = 1
        while p2<=len(nums)-1:
            if nums[p1] == nums[p2]:
                nums.pop(p2)
            else:
                p1+=1
                p2+=1      
        return len(nums)
obj = Solution()
nums = [1,1,2]
print(obj.removeDuplicates(nums))