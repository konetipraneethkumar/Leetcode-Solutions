class Solution(object):
    def shuffle(self, nums, n):
        ans= []
        for i in range(n):

            ans.append(nums[i])

            ans.append(nums[n +i])
        return ans
        

        



nums = [2,5,1,3,4,7]
n = len(nums) //2
obj = Solution()
print(obj.shuffle(nums, n))