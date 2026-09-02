class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        res = [-1] *n
        
        window = 2 * k +1
        if window > n:
            return [-1] * n
        
        win_sum = sum(nums[:window])
        avg = win_sum // window
        res[k] = avg
        for i in range(k+1, n-k):
            
            win_sum +=nums[i+k]
            win_sum-=nums[i-k-1]
            res[i] = win_sum // window
        return res

