class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        water = 0
        while left < right:
            water_temp = min(height[left], height[right]) * (right - left)
            if water < water_temp:
                water = water_temp
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return water


            