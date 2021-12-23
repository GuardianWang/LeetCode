"""
LC 16
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    close_s = float('inf')
    for i in range(len(arr) - 2):
        j, k = i + 1, len(arr) - 1
        while j < k:
            s = arr[i] + arr[j] + arr[k]
            diff = abs(s - target_sum)
            diff_close = abs(close_s - target_sum)
            if diff < diff_close or (diff == diff_close and s < close_s):
                close_s = s
            if s < target_sum:
                j += 1
            elif s > target_sum:
                k -= 1 
            else:
                return target_sum
    return close_s


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()



"""
Time O(N^2)
Space O(N)
"""

