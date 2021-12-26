"""
LC 259
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    cnt = 0
    for i in range(len(arr) - 2):
        # Early stop
        if arr[i] > target / 3:
            break
        j, k = i + 1, len(arr) - 1
        while j < k:
            s = arr[i] + arr[j] + arr[k]
            if s < target:
                cnt += k - j  # fix j, k = j + 1...k
                j += 1
            else:
                k -= 1
    return cnt


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()


"""
Time O(N^2)
Space O(N)
"""

