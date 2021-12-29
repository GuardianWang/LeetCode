"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
"""


def find_first_smallest_missing_positive(nums):
    # although nums[i] is not bounded, 
    # the answer is bounded by [1, len(nums) + 1]
    # len(nums) + 1 when all len(nums) appear

    # set negative to 0 to make sure when adding M to
    # this position, value >= M
    for i, n in enumerate(nums):
        if n < 0:
            nums[i] = 0
        elif nums[i] > len(nums):
            nums[i] = len(nums) + 1
    M = len(nums) + 2
    print(nums)
    for i, n in enumerate(nums):
        if 0 < n % M <= len(nums):
            nums[n % M - 1] += M
    for i, n in enumerate(nums):
        if n < M:
            return i + 1
    return len(nums) + 1


def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()


"""
Time O(N)
Space O(1)
"""

