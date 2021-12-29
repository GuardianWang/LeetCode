"""
We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""


def cyclic_sort(nums):
    for p in range(len(nums)):
        while nums[p] != p + 1:
            swap(nums, p, nums[p] - 1)

    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()


"""
Time O(N): One operation will place one number at the 
right place. Once a number is at the correct place,
it will not be moved.
Space O(1)
"""

