class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        rain = 0
        left = 0
        right = n-1
        leftMax = height[0]
        rightMax = height[right]

        while left < right:
            if leftMax > rightMax:
                right -= 1
                rightMax = max(rightMax, height[right])
                rain += rightMax - height[right]
            else:
                left +=1
                leftMax = max(leftMax, height[left])
                rain += leftMax - height[left]
        
        return rain
            

        
        