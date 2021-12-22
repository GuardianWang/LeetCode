"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""

def non_repeat_substring(str1):
    win_start = 0
    max_len = 0
    c2freq = dict()
    for win_end, c in enumerate(str1):
        if c not in c2freq:
            c2freq[c] = 1
            max_len = max(max_len, win_end - win_start + 1)
        else:
            c2freq[c] += 1
            while c2freq[c] > 1:
                c2freq[str1[win_start]] -= 1
                if c2freq[str1[win_start]] == 0:
                    del c2freq[str1[win_start]]
                win_start += 1
    return max_len


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))  # 3
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))  # 2
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))  # 3


main()

"""
Time O(N)
Space O(N)
"""

