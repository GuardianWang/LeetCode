"""
LC 713
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""


def find_subarrays(arr, target):
    win_start = 0
    product = 1
    res = []
    for win_end, n in enumerate(arr):
        product *= n 
        while product >= target and win_start < win_end:
            product /= arr[win_start]
            win_start += 1
        if product < target:
            res.extend([[arr[j] for j in range(i, win_end + 1)] for i in range(win_start, win_end + 1)])
    return res


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()


"""
Time O(N^3): create space
Space O(N^3): N^2 arrays * N length
"""

