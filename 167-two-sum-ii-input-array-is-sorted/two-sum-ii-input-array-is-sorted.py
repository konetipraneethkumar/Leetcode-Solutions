class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) -1

        while(i != j):
            sum = numbers[i] + numbers[j]
            if sum < target:
                i+=1
            elif(sum > target):
                j-=1
            elif sum == target:
                return [i+1 , j+1]
        return False
numbers = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))
  