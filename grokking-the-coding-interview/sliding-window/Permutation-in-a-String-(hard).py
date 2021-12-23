"""
LC 567
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def find_permutation(s, pattern):
    if len(s) < len(pattern):
        return False

    win_start = 0
    p_freq = dict()
    remain = len(pattern)  # sum of absolute frequency
    for c in pattern:
        if c not in p_freq:
            p_freq[c] = 0
        p_freq[c] += 1

    for win_end, c in enumerate(s):
        if c in p_freq:
            if p_freq[c] > 0:
                remain -= 1
            p_freq[c] -= 1 

        if win_end >= len(pattern) - 1:  # 0-indexed
            if remain == 0:
                return True
            if s[win_start] in p_freq:
                if p_freq[s[win_start]] >= 0:
                    remain += 1
                p_freq[s[win_start]] += 1
            win_start += 1  # increase win_start at the end, increase win_end at the beginning
            
    return False 


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))  # True 
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))  # False 
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))  # True 
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))  # True 
  print('Permutation exist: ' + str(find_permutation("ioippgg", "oii")))  # True 


main()


"""
Time O(M + N): decrease the remaining count instead of checking equality between dicts 
Space O(M)
"""

