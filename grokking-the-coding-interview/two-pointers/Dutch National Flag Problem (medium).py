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
    p_place = 0
    for target in [0, 1]:
        for p_iter in range(p_place, len(arr)):
            if arr[p_iter] == target:
                arr[p_place], arr[p_iter] = arr[p_iter], arr[p_place]
                p_place += 1
    return arr


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

