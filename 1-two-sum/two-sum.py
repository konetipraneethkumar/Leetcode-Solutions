class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #left = 0
      #right = len(nums) - 1
      #
      #while left < right:
      #    sum = nums[left] + nums[right]

      #    if sum == target:
      #        return [left,right]

      #    elif sum > target:
      #        right -=1

      #    elif sum < target:
      #        left +=1
      #return None # This approach will work for only sorted array 
      

      # Using Hash Table
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in hash_table and hash_table[target - nums[i]] != i:
                return [i,hash_table[target - nums[i]]]
        
