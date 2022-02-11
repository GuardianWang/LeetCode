"""
LC 84
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
"""
class Solution:
    def largestRectangleArea(self, heights) -> int:
        # find left and right of a bar
        # use increasing stack to save left
        # compare top and current to find right
        stack = [(-1, -1)]  # id, val
        ans = 0
        heights.append(0)  # in case heights are increasing
        for r, h in enumerate(heights):
            while h < stack[-1][1]:
                center_h = stack.pop()[1]
                ans = max(ans, center_h * (r - stack[-1][0] - 1))
            stack.append((r, h))
        return ans


"""
Time/Space O(N)
"""

