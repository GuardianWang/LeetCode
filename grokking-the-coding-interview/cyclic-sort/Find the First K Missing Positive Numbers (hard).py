"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""


def find_first_k_missing_positive(nums, k):
    for i, n in enumerate(nums):
        j = nums[i] - 1
        while 0 < n <= len(nums) and n != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            n = nums[i]
            j = n - 1

    res = []
    for i, n in enumerate(nums):
        if len(res) == k:
            break
        if i != n - 1:
            res.append(i + 1)
    
    if len(res) < k:
        # a large number may appear 
        occurred = set(nums)
        next_num = len(nums) + 1
    while len(res) < k:
        while next_num in occurred:
            next_num += 1
        res.append(next_num)
        next_num += 1
    return res 


def main():
  # [1, 2, 6]
  # [1, 5, 6]
  # [1, 2]
  # [1, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))
  print(find_first_k_missing_positive([-2, -3, 4, 2, 9], 15)) # [1,5]中有1,3,5;
                                                              # [6,..]中跳过数组中已有的9


main()


"""
Time O(N + klogk)
Space O(k)
"""

