class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        l1, r1, l2, r2 = 0, len(nums) - k - 1, len(nums) - k, len(nums) - 1
        while l1 <= r1 and l2 <= r2:
            l1, r1, l2, r2 = self.swap_interval(nums, l1, r1, l2, r2)
        
    def swap_interval(self, nums, l1, r1, l2, r2):
        r11, r22 = r1, r2
        while l1 <= r11 and l2 <= r22:
            self.swap(nums, r11, r22)
            r11 -= 1
            r22 -= 1
        if r11 < l1 and r22 < l2:
            return l1, r11, l2, r22
        elif r11 < l1:  # left is shorter
            return l1, r1, l2, r22
        else:  # right is shorter
            return l1, r11, r11 + 1, r22
        
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]
        

"""
Time O(N)
Space O(1)
"""
