"""
LC 658
Problem Statement
Given an array of numbers sorted in ascending order,
find the element in the array that has the minimum difference with the given ‘key’.
Example 1:
Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
Example 2:
Input: [4, 6, 10], key = 4
Output: 4
Example 3:
Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:
Input: [4, 6, 10], key = 17
Output: 10
"""
def search_min_diff_element(arr, key):
    if arr[0] >= key:
        return arr[0]
    if arr[-1] <= key:
        return arr[-1]

    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) >> 1
        if arr[m] - key < 0:
            l = m + 1
        else:
            r = m - 1
    return arr[r] if abs(arr[r] - key) <= abs(arr[l] - key) else arr[l]


def search_closest_k(arr, k, x):
    # Time O(log(N-k)) + k
    # Space O(k)
    # find left index
    l, r = 0, len(arr) - k
    while l < r:
        # m < r, m + k < len(arr)
        m = (l + r) >> 1
        if arr[m] - x + arr[m + k] - x >= 0:
            r = m
        else:
            l = m + 1
    return arr[l: l + k]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()


"""
Time O(logN)
Space O(1)
"""
