"""
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

def longest_substring_with_k_distinct(str1, k):
    if k >= len(str1):
        return len(str1)
    char2freq = dict()
    win_start = 0
    max_len = 0
    for win_end, char_end in enumerate(str1):
        if char_end not in char2freq:
            char2freq[char_end] = 0
        char2freq[char_end] += 1

        if len(char2freq) <= k:
            max_len = max(max_len, win_end - win_start + 1)

        while len(char2freq) > k:
            char2freq[str1[win_start]] -= 1
            if char2freq[str1[win_start]] == 0:
                del char2freq[str1[win_start]]
            win_start += 1

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

