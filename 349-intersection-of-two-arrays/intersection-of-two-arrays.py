class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = []
        set1 = set()
        set2 = set()
        for x in nums1:
            if x in set1:
                continue
            set1.add(x)
        for x in nums2:
            if x in set2:
                continue
            set2.add(x)
        hashset =  list(set1 & set2)
        return hashset
            


        