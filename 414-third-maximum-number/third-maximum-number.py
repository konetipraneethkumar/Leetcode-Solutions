class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -float('inf')
        second_largest = -float('inf')
        third_largest = -float('inf')
        for i in range(len(nums)):
            if nums[i] == largest or nums[i] == second_largest or nums[i] == third_largest:
                continue

            if nums[i] > largest:
                third_largest = second_largest
                second_largest = largest
                largest = nums[i]
            elif nums[i]<largest and nums[i]>second_largest:
                third_largest = second_largest
                second_largest = nums[i]
            elif nums[i]<largest and nums[i]<second_largest and nums[i]> third_largest:
                third_largest = nums[i]

        if third_largest != -float('inf'):
            return third_largest
        else:
            return largest
