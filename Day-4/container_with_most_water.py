class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxi = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxi = max(maxi, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxi
