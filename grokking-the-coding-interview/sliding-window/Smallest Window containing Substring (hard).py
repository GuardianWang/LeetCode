"""
LC 76
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""


def find_substring(str1, pattern):
    win_start = 0
    p_freq = dict()
    for c in pattern:
        if c not in p_freq:
            p_freq[c] = 0
        p_freq[c] += 1
    remains = len(pattern)  # sum of absolute value of frequency

    min_len = float('inf')
    min_str = ""
    c2freq = dict()
    for win_end, c in enumerate(str1):
        if c in p_freq:
            if p_freq[c] > 0:
                remains -= 1
            p_freq[c] -= 1

        while remains == 0:
            win_len = win_end - win_start + 1
            if win_len < min_len:
                min_len = win_len
                min_str = str1[win_start: win_end + 1]
            lchar = str1[win_start]
            if lchar in p_freq:
                if p_freq[lchar] >= 0:
                    remains += 1
                p_freq[lchar] += 1
            win_start += 1
    return min_str 
        

def main():
  print(find_substring("aabdec", "abc"))  # abdec
  print(find_substring("abdbca", "abc"))  # bca 
  print(find_substring("adcad", "abc"))  # ""

main()


"""
Time O(N+M)
Space O(N)
"""

