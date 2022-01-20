"""
LC 769
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.



Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
"""
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        # the values in a chunk has the same range of index
        l, r = 0, 0
        ans = 0
        cnt_chunk = 0
        for i, n in enumerate(arr):
            cnt_chunk += 1
            if l <= n <= r and cnt_chunk == r - l + 1:
                # all values have the same range of indices
                ans += 1
                l, r = r + 1, r + 1
                cnt_chunk = 0
            elif n > r:
                # extend chunk to the right
                r = n
        return ans


"""
Time O(N)
Space O(1)
"""

