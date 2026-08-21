class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i] **2
        """  
        for i in range(len(nums)):
            for j in range(i+1,len(nums) ):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        """
        nums.sort()
        return nums
        


        
            
        return nums



        