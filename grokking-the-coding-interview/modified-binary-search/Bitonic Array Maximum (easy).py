"""
LC 852
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
Example 1:
Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:
Input: [3, 8, 3, 1]
Output: 8
Example 3:
Input: [1, 3, 8, 12]
Output: 12
Example 4:
Input: [10, 9, 8]
Output: 10
"""
def find_max_in_bitonic_array(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = l + ((r - l) >> 1)
        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return arr[l]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()


"""
Time O(logN)
Space O(1)
"""
