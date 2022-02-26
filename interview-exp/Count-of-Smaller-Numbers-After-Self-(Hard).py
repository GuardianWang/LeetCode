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
        # binary index tree
        # unique values
        values = sorted(set(nums))
        v2treeid = {v: i + 1 for i, v in enumerate(values)}
        
        bit = [0] * (len(values) + 1)  # want an 1-indexed array

        def update(v):
            treeid = v2treeid[v]
            while treeid < len(bit):
                bit[treeid] += 1
                treeid += treeid & -treeid
                
        def query(v):
            treeid = v2treeid[v]
            ans = 0
            while treeid > 0:
                # query a smaller one
                ans += bit[treeid]
                treeid -= treeid & -treeid
            return ans
        
        # get result
        ans = [0] * len(nums)
        for i in reversed(range(len(nums))):
            n = nums[i]
            update(n)
            if v2treeid[n] > 1:
                ans[i] = query(values[v2treeid[n] - 2])
        return ans


"""
Time O(NlogN)
Space O(N)
"""
