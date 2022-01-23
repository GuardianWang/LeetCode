"""
LC 1291
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""
class Solution:
    def sequentialDigits(self, low: int, high: int):
        base = "123456789"
        l, r = 0, len(str(low)) - 1
        ans = []
        while r < len(base):
            n = int(base[l: r + 1])
            if n > high:
                break
            elif n >= low:
                ans.append(n)
            if r + 1 == len(base):
                if l == 0:
                    break  # longest
                r = r - l + 1
                l = 0
            else:
                l += 1
                r += 1

        return ans


"""
Time/Space O(1): finite
"""
        
