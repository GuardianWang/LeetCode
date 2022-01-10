"""
LC 268
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""
def find_missing_number(nums):
    m = len(nums)
    for i, n in enumerate(nums):
        m ^= i ^ n
    return m 


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()


"""
Time O(N)
Space O(1)
"""

