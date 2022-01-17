"""
LC 215
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
Example 1:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
Example 2:
Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three smaller numbers are
[1, 2, 5].
Example 3:
Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""
from random import randint  # inclusive


def find_Kth_smallest_number(nums, k):
    l, r = 0, len(nums) - 1
    while l <= r:
        # l <= p <= r
        p = partition(nums, l, r)
        if p < k - 1:
            l = p + 1
        elif p > k - 1:
            r = p - 1
        else:
            return nums[p]


def partition(nums, l, r):
    p = randint(l, r)
    swap(nums, p, r)
    for i in range(l, r):
        # nums[j] < nums[r], j < l
        # nums[j] >= nums[r], l= < j < i
        if nums[i] < nums[r]:
            swap(nums, l, i)
            l += 1
    swap(nums, l, r)
    return l


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()


"""
Time O(N) ave O(N^2) worst
Space O(1)
"""
