"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""


def shortest_window_sort(arr):
    m, M = float('inf'), -float('inf')
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            m = min(m, arr[i + 1])
            M = max(M, arr[i])
    if m == float('inf'):
        return 0

    l, r = -1, len(arr)
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1] and arr[i] <= m:
            l = i
        else:
            break
    for i in range(len(arr) - 1, 0, -1):
        if M <= arr[i] and arr[i - 1] <= arr[i]:
            r = i
        else:
            break
    return r - l - 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()


"""
Time O(N)
Space O(1)
"""

