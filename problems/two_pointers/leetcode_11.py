class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l =0 
        r = len(height) - 1
        maxi = 0
        while l < r :
            diff = r - l
            h = min(height[l] , height[r])
            area = h * diff
            maxi = max(area, maxi)

            if height[l] < height[r]:
                l += 1
            else :
                r -=1
        return maxi