"""
LC 6015
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    
Example 2:

Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.
"""
class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
    	# if sum: save remainder
        gcd2n = defaultdict(int)
        for n in nums:
            gcd2n[gcd(n, k)] += 1
        cnt = 0
        for (i, n1), (j, n2) in combinations_with_replacement(gcd2n.items(), 2):
            if i * j % k > 0:
                continue
            if i == j:
                cnt += n1 * (n1 - 1) // 2
            else:
                cnt += n1 * n2
        return cnt


"""
K=prod(pi^di)
S=prod(di)
Time: O(N+S^2)
Space O(S)
"""
