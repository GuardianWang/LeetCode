"""
LC 34
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
Example 1:
Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:
Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:
Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
"""
def find_range(arr, key):
    if not arr or arr[-1] < key or arr[0] > key:
        return [-1, -1]
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (r + l) >> 1
        if key < arr[m]:
            r = m - 1
        else:
            l = m + 1
    # when l == r and key < arr[m], want m - 1, i.e. r
    # when key == arr[m], change l
    if arr[r] != key:
        return [-1, -1]
    right = r

    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) >> 1
        if key <= arr[m]:
            r = m - 1
        else:
            l = m + 1
    # when l == r and key < arr[m], want m, i.e. l
    # when key == arr[m], change r
    return [l, right]


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()


"""
Time O(logN)
Space O(1)
"""
