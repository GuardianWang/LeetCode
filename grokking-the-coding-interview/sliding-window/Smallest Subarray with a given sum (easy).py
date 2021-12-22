"""
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
    smallest_sum = float('inf')
    # window [win_start, win_end)
    while win_end < len(arr):
        # extend 
        while window_sum < s:
            window_sum += arr[win_end]
            win_end += 1
        
        smallest_sum = min(smallest_sum, window_sum)

        # shirink
        while window_sum >= s:
            print(window_sum, win_start, win_end)
            smallest_sum = min(smallest_sum, window_sum)
            window_sum -= arr[win_start]
            win_start += 1
            # win_start <= win_end

        
    return smallest_sum


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))  # 2
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))  # 1
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))  # 3

  
main()

