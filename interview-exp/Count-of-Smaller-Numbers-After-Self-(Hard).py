"""
LC 315
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = [n, i, 0]
        self.merge_sort(nums, 0, len(nums) - 1)
        ans = [0] * len(nums)
        for _, idx, cnt in nums:
            ans[idx] = cnt
        return ans
        
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        m = (l + r) >> 1
        self.merge_sort(nums, l, m)
        self.merge_sort(nums, m + 1, r)
        
        # merge
        i, j = 0, 0
        nums_l = nums[l: m + 1].copy()
        nums_r = nums[m + 1: r + 1].copy()
        inverse_cnt = 0  # count inverse
        cur_id = l
        while i < len(nums_l) or j < len(nums_r):
            if j >= len(nums_r) or (i < len(nums_l) and nums_l[i][0] <= nums_r[j][0]):
                nums[cur_id] = nums_l[i]
                nums[cur_id][-1] += inverse_cnt
                i += 1
            else:
                nums[cur_id] = nums_r[j]
                j += 1
                inverse_cnt += 1
            cur_id += 1


"""
Time O(NlogN)
Space O(N)
"""
