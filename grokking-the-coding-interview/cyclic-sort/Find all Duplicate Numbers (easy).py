"""
LC 442
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


def find_all_duplicates(nums):
    M = len(nums) + 1
    for i, n in enumerate(nums):
        nums[n % M - 1] += M
    lim = 2 * M
    return [i + 1 for i, n in enumerate(nums) if n > lim]


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()


"""
Time O(N)
Space O(1)
"""

