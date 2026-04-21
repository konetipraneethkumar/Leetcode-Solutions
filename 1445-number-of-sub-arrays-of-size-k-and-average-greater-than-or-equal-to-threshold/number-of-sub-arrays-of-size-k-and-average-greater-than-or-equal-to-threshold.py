class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        w_st = 0
        w_avg = 0
        w_sum = 0
        r_avg = threshold
        for i in range(len(arr)):
            w_sum += arr[i]
            if i >= k-1:
                w_avg = w_sum / k
                if w_avg >= r_avg:
                    count += 1
                w_sum -= arr[w_st]
                w_st += 1
        return count
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
s = Solution()
print(s.numOfSubarrays(arr, k, threshold))