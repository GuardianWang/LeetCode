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
    for i, n in enumerate(nums):
        j = nums[i] - 1
        # only deal with legal indices
        while 0 < n <= len(nums) and n != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            n = nums[i]
            j = n - 1

    for i, n in enumerate(nums):
        if i != n - 1:
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

