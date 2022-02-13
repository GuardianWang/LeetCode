"""
LC 6005
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 
"""
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        cnt0 = Counter(nums[::2])
        cnt1 = Counter(nums[1::2])
        num0, n0 = cnt0.most_common(1)[0]
        num1, n1 = cnt1.most_common(1)[0]
        len0 = (len(nums) + 1) // 2
        len1 = len(nums) - len0
        if num0 != num1:
            return len(nums) - n0 - n1
        elif len0 - n0 < len1 - n1:
            return len(nums) - n0 - cnt1.most_common(2)[1][1]
        elif len0 - n0 > len1 - n1:
            return len(nums) - n1 - cnt0.most_common(2)[1][1]
        elif len(cnt0) > 1:
            return len(nums) - n1 - cnt0.most_common(2)[1][1]
        elif len(cnt1) > 1:
            return len(nums) - n0 - cnt1.most_common(2)[1][1]
        else:
            return min(n0, n1)
            
        
"""
Time O(N) if use heapq to count
Space O(1) if use heapq to count
"""
