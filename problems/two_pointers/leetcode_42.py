class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        maxL = 0
        maxR = 0 
        l = 0
        r = len(height) - 1
        arr = 0
        while l < r:
            if height[l] <= height[r]:
                maxL = max(maxL, height[l])
                diff = maxL - height[l]
                if diff < 0:
                    diff = 0
                arr += diff
                l += 1
            else: 
                maxR = max(maxR, height[r])
                diff = maxR - height[r]
                if diff < 0:
                    diff = 0
                arr += diff
                r -= 1
        return arr