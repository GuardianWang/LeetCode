"""
LC 448
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4
"""


def find_missing_numbers(nums):
    # mark 
    for i, n in enumerate(nums):
        # don't forget module
        nums[n % len(nums) - 1] += len(nums)
    return [i + 1 for i, n in enumerate(nums) if n <= len(nums)]


def main():
    # [4, 6, 7]
    # [3]
    # [4]
    # [2, 3, 4, 5, 7]
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))
    print(find_missing_numbers([6,6,6,6,6,6,8,9,1]))


main()


"""
Time O(N)
Space O(1)
"""

