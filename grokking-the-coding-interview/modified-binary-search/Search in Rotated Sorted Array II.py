"""
LC 81
search in a sorted and rotated array that also has duplicates?
Example 1:

Input: [3, 7, 3, 3, 3], key = 7
Output: 1
Explanation: '7' is present in the array at index '1'.
"""
def search_rotated_with_duplicates(arr, key):
  # make sure arr[l] > arr[-1]
  l = 0
  while l < len(arr) and arr[l] == arr[-1]:
    l += 1
  start = l
  # in case starting from l, arr[l:] is sorted
  if 0 < l < len(arr) and arr[l - 1] > arr[l]:
    l, r = l - 1, l - 1
  else:
    r = len(arr) - 1
  # find peak
  while l < r:
    m = r - (r - l >> 1)
    if arr[m] < arr[start]:
      r = m - 1
    else:
      l = m

  h = r
  idx = binary_search(arr, key, 0, h)
  if idx == -1:
    idx = binary_search(arr, key, h + 1, len(arr) - 1)
  return idx


def binary_search(arr, key, l, r):
  if l > r:
    return -1
  while l < r:
    m = l + (r - l >> 1)
    if key <= arr[m]:
      r = m 
    else:
      l = m + 1
  if arr[l] == key:
    return l
  else:
    return -1


def main():
  print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))
  print(search_rotated_with_duplicates([3, 3, 3, 7, 3, 3, 3, 3, 3, 3], 7))


main()


"""
Time O(N)
Space O(1)
"""

