"""
LC 340
Given a string, find the length of the longest substring in it with no more than K  characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""
from collections import defaultdict


def longest_substring_with_k_distinct(str1, k):
    if k >= len(set(str1)):
        return len(str1)
    if k == 0:
        return 0
    
    max_len = 0
    c2cnt = defaultdict(int)
    l = 0
    
    for r, c in enumerate(str1):
        c2cnt[c] += 1
        if len(c2cnt) > k:
            c2cnt[str1[l]] -= 1
            if c2cnt[str1[l]] == 0:
                del c2cnt[str1[l]]
            l += 1
        else:
            max_len = max(max_len, r - l + 1)
    return max_len


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))  # 4
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))  # 2
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))  # 5


main()

"""
Time O(N): move win_start one by one
Space O(K)
"""

