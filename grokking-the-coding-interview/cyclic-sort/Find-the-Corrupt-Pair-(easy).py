"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""


def find_corrupt_numbers(nums):
    M = len(nums) + 1
    for i, n in enumerate(nums):
        nums[n % M - 1] += M

    miss, dupl = 0, 0
    lim = 2 * M
    for i, n in enumerate(nums):
        if n < M:
            miss = i + 1
        elif n > lim:
            dupl = i + 1
    return [dupl, miss]
    

def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()


"""
Time O(N)
Space O(1)
"""

