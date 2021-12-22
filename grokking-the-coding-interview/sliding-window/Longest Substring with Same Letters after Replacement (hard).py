"""
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


def length_of_longest_substring(str1, k):
    # k + 1 distinct letters
    win_start = 0
    max_len = 0
    max_freq = 0
    c2freq = dict()
    for win_end, c in enumerate(str1):
      if c not in c2freq:
        c2freq[c] = 0
      c2freq[c] += 1
      # max frequency ever in a window
      max_freq = max(max_freq, c2freq[c])

      win_len = win_end - win_start + 1
      if win_len - max_freq > k:
        # because we only need the max length,
        # we can simply keep the max length ever
        # win_len - max_current >= win_len - max_freq > k
        # win_len and max_freq remain the same until 
        # new max_freq appears, i.e., max_current
        # win_len - max_current = win_len - max_freq <= k

        c2freq[str1[win_start]] -= 1
        win_start += 1
      else:
        max_len = max(max_len, win_len)

    return max_len


def main():
  print(length_of_longest_substring("aabccbb", 2))  # 5
  print(length_of_longest_substring("abbcb", 1))  # 4
  print(length_of_longest_substring("abccde", 1))  # 3


main()


"""
Time O(N)
Space O(1): 26 letters
"""

