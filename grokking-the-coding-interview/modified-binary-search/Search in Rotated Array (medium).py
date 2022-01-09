"""
LC 33
Search in Rotated Array (medium)
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
find if a given ‘key’ is present in it.
Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1.
You can assume that the given array does not have any duplicates.
Example 1:
Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.
Example 2:
Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
"""
def search_rotated_array(arr, key):
  # find peak
  l, r = 0, len(arr) - 1
  while l < r:
    m = r - (r - l >> 1)
    if arr[m] > arr[0]:
      l = m
    else:
      r = m - 1
  idx = find_val(arr, key, 0, l)
  if idx == -1:
    idx = find_val(arr, key, l + 1, len(arr) - 1)
  return idx


def find_val(arr, key, l, r):
  if l > r:
    return -1
  while l < r:
    m = r - (r - l >> 1)
    if key < arr[m]:
      r = m - 1
    else:
      l = m
  return l if arr[l] == key else -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))



main()


"""
Time O(logN)
Space O(1)
"""
