"""
LC 6012
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

 

Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
"""
class Solution:
    def countEven(self, num: int) -> int:
    	# every 10 values, lowest digit ranging from 0 to 9, there are 5
        base_cnt = (num // 10) * 5
        # the previous closes ending with 0
        base_n = num - num % 10
        is_even = 1 if sum(map(int, str(base_n))) % 2 == 0 else 0
        return base_cnt + ((num - base_n + 1) // 2) + is_even * ((num - base_n + 1) % 2 == 1) - 1  # 0
        

"""
Time/Space O(1)
"""
