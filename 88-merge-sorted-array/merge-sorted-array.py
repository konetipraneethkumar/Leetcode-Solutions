class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res= []
        n1 = 0
        n2 = 0
        while n1 < m and n2 < n:
            if nums1[n1] <= nums2[n2]:
                res.append(nums1[n1])
                n1 +=1
            else:
                res.append(nums2[n2])
                n2 +=1
        while n1 < m:
            res.append(nums1[n1])
            n1+=1
        while n2 < n:
            res.append(nums2[n2])
            n2+=1
        nums1[:] = res
        return 
        
    

        


        