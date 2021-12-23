"""
LC 209
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].
"""


def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    win_start = 0
    win_end = 0
    smallest_len = float('inf')
    # window [win_start, win_end)
    for win_end in range(len(arr)):
        # extend 
        window_sum += arr[win_end]
        while window_sum >= s:  # one while is enough, like a combination of if and for
            smallest_len = min(smallest_len, win_end - win_start + 1)
            window_sum -= arr[win_start]
            win_start += 1
    return smallest_len if smallest_len < float('inf') else 0
"""
Time complexity:
for loop: win_end increases N times
while loop: win_start increases at most N times
"""


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))  # 2
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))  # 1
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))  # 3

  
main()

