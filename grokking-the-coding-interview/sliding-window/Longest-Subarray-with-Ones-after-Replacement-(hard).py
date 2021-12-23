"""
LC 1004
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def length_of_longest_substring(arr, k):
    freq0 = 0
    max_len = 0
    win_start = 0
    for win_end, c in enumerate(arr):
        if c == 0:
            freq0 += 1
        if freq0 > k:
            if arr[win_start] == 0:
                freq0 -= 1
            win_start += 1
        else:
            max_len = max(max_len, win_end - win_start + 1)
    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))  # 6
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))  # 9


main()


"""
Time O(N)
Space O(1)
"""

