class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold

        window_sum = sum(arr[:k])
        if window_sum >= target:
            count = 1 
        else:
            count = 0

        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]

            if window_sum >= target:
                count += 1

        return count