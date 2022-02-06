"""
LC 6001
Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

 

Example 1:

Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:

Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
"""
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        s = str(num)
        if num < 0:
            ns = sorted(map(int, s[1:]), key=lambda x: -x)
            return -int("".join(map(str, ns)))
        n0 = s.count('0')
        ns = sorted(map(int, s))
        ns.insert(0, ns.pop(n0))
        return int("".join(map(str, ns)))
        

"""
Time O(logN loglogN)
Space O(logN)
"""
