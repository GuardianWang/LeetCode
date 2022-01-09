"""
LC 154
How do we find the rotation count of a sorted and rotated array that has duplicates too?

The above code will fail on the following example!

Example 1:

Input: [3, 3, 7, 3]
Output: 3
Explanation: The array has been rotated 3 times
"""
def count_rotations_with_duplicates(arr):
  if arr[0] < arr[-1]:
    return 0
  for l in range(len(arr)):
    if arr[l] != arr[-1]:
      break 
  if l == len(arr) - 1:
    return 0  # all values are the same
  elif l > 0 and arr[l - 1] > arr[l]:
    return l  # l is smallest
  
  s = l 
  r = len(arr) - 1
  while l < r:
    m = l + (r - l >> 1)
    if arr[m] < arr[s]:
      r = m 
    else:
      l = m + 1

  return l


def main():
  # 3 2 1 3 1 0
  print(count_rotations_with_duplicates([3, 3, 7, 3]))
  print(count_rotations_with_duplicates([3, 7, 3]))
  print(count_rotations_with_duplicates([7, 3, 3]))
  print(count_rotations_with_duplicates([3, 3, 7, 3, 3, 3, 3]))
  print(count_rotations_with_duplicates([7, 3, 3, 3, 3, 3]))
  print(count_rotations_with_duplicates([3, 3, 3, 3]))


main()


"""
Time O(N)
Space O(1)
"""

