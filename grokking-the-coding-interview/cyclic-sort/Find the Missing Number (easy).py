"""
LC 268
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""


def find_missing_number(nums):
    for i, n in enumerate(nums):
        while n < len(nums) and i != n:
            nums[i], nums[n] = nums[n], nums[i]
            n = nums[i]
    
    for i, n in enumerate(nums):
        if i != n:
            return i
    return len(nums)


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()


"""
Time O(N)
Space O(1)
"""

