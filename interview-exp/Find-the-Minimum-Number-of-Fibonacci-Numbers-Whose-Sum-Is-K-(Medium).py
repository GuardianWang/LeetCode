"""
LC 1414
Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 for n > 2.
It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
 

Example 1:

Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.
Example 2:

Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:

Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
"""
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k <= 3:
            return 1
        # fib numbers
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        # greedy to find nearest smaller one
        cnt = 0
        while k > 0:
            cnt += 1
            idx = max(bisect_right(fibs, k) - 1, 0)
            k -= fibs[idx]
        return cnt
        

"""
Time/Space O(logN)
"""
