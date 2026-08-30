class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
        re_order = []   
        for key, val in freq.items():
            re_order.append([val,key])

        re_order = sorted(re_order, reverse=True)
        res = []
        for item in re_order:
            res.append(item[1])
            if len(res) == k:
                return res
        return

            
