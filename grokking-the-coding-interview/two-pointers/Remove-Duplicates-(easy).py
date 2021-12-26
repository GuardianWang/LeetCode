"""
LC 26
Given an array of sorted numbers,
remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


def remove_duplicates(arr):
    p_place = 0
    last_n = float('inf')
    for p_iter, n in enumerate(arr):
        if n != last_n:
            arr[p_place] = n 
            last_n = n
            p_place += 1
    return p_place


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
  print(remove_duplicates([2, 2, 2, 11]))  # 2


main()

"""
Time O(N)
Space O(1)
"""

