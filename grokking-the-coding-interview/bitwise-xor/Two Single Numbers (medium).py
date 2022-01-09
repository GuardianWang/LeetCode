"""
LC 260
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.
Example 1:
Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:
Input: [2, 1, 3, 2]
Output: [1, 3]
"""
def find_single_numbers(nums):
    ns = 0
    for n in nums:
        ns ^= n
    # find a different digit (XOR is 1)
    right = 1
    while right & ns == 0:
        right <<= 1
    n1, n2 = 0, 0

    # XOR with the num that have one digit in common
    # use this digit to divide into 2 equivalent groups,
    # each group with 1 number missing
    for n in nums:
        if n & right == 0:  # this digit is 0
            n1 ^= n
        else:  # digit is 1
            n2 ^= n
    return [n1, n2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()


"""
Time O(N)
Space O(1)
"""
