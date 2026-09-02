class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        iseven = lambda n:n%2 == 0 
        st = 0
        ed = len(nums)-1
        while st < ed:
            if iseven(nums[st]):
                st+=1
            elif iseven(nums[ed]) :
                nums[st], nums[ed] = nums[ed], nums[st]
                st+=1
                ed-=1
            else:
                ed-=1
                
               
        return nums
        