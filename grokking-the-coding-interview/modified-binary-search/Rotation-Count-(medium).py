"""
LC 153
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
You can assume that the array does not have any duplicates.
Example 1:
Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
Example 2:
Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.
Example 3:
Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
"""
def count_rotations(arr):
  l, r = 0, len(arr) - 1 
  # starting index of the second half
  while l <= r:
    m = l + (r - l >> 1)
    if arr[m] <= arr[-1]:
      r = m - 1 
    else:
      l = m + 1 
  return l

def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))
  print(count_rotations([1, 3, 8, 10, -1]))  # 4


main()


"""
Time O(logN)
Space O(1)
"""

