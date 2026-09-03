class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #if len(nums)<2:
        #    return
        #l = 0
        #for r in range(1, len(nums)):
        #    
        #    if nums[l] ==0 and nums[r] != 0:
        #        nums[l], nums[r] = nums[r],nums[l]
        #        l+=1
        #    elif nums[l] !=0:
        #        l+=1
        #return
        l = 0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return