"""
LC 1095
Search Bitonic Array (medium)
Given a Bitonic array, find if a given ‘key’ is present in it.
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.
Example 1:
Input: [1, 3, 8, 4, 3], key=4
Output: 3
Example 2:
Input: [3, 8, 3, 1], key=8
Output: 1
Example 3:
Input: [1, 3, 8, 12], key=12
Output: 3
Example 4:
Input: [10, 9, 8], key=10
Output: 0
"""
def search_bitonic_array(arr, key):
  # max id
  l, r = 0, len(arr) - 1
  while l < r:
    m = l + (r - l >> 1)
    if arr[m] < arr[m + 1]:
      l = m + 1
    else:
      r = m

  idx = find_val(arr, key, 0, l)
  if idx == -1:
    idx = find_val(arr, key, l, len(arr) - 1)
  return idx


def find_val(arr, key, l, r):
  ascend = arr[l] <= arr[r]
  while l < r:
    m = l + (r - l >> 1)
    if ascend:
      if key <= arr[m]:
        r = m
      else:
        l = m + 1
    else:
      if key < arr[m]:
        l = m + 1
      else:
        r = m

  return l if arr[l] == key else -1


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()


"""
Time O(logN)
Space O(1)
"""
