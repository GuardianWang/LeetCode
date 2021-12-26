"""
LC 75
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2,]
"""


def dutch_flag_sort(arr):
    l, r = 0, len(arr) - 1
    # l: next place to put 0
    # r: next place to put 2
    # 1s are within [l, r]
    i = 0
    while i <= r:  # not <
        if arr[i] == 0:
            swap(arr, l, i)
            l += 1
            i += 1  # make sure l <= i
        elif arr[i] == 2:
            swap(arr, r, i)
            r -= 1
        else:
            i += 1
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()


"""
Time O(N)
Space O(1)
"""

