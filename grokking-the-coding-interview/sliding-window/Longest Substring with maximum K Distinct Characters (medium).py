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
    char2endid = dict()
    win_start = 0
    max_len = 0
    for win_end in range(len(str1)):
        char2endid[str1[win_end]] = win_end
        if len(char2endid) > k:
            win_start = char2endid[str1[win_start]] + 1
            char_to_del = [k for k, v in char2endid.items() if v < win_start]
            for c in char_to_del:
                del char2endid[c]
        else:
            max_len = max(max_len, win_end - win_start + 1)

    return max_len


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))  # 4
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))  # 2
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))  # 5


main()

"""
Time O(NK): need to iterate K chars to find which to delete
Space O(K)
