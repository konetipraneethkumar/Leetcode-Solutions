class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        r = k
        wSum : float= 0
        mSum : float =float('-inf')
        for i in range(l,r):
            wSum = wSum + nums[i]
        mSum = wSum
        while r < len(nums):
            
           
            wSum -= nums[l]
            wSum +=nums[r]
            
            l+=1
            r+=1
            if wSum/k > mSum/k:
                mSum = wSum
        return mSum/k


        

        