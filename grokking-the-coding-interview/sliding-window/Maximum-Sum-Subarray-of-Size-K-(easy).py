"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""
def max_sub_array_of_size_k(k, arr):
    s = 0
    M = -float('inf')
    for winEnd in range(len(arr)):
        s += arr[winEnd]
        if winEnd >= k - 1:
            M = max(M, s)
            s -= arr[winEnd - k + 1]  # in the if statement
    return M


arr = [2, 1, 5, 1, 3, 2]
k = 3
res = max_sub_array_of_size_k(k, arr)
print(res)

