"""
LC 438
Given a string and a pattern, find all  of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""


def find_string_anagrams(str1, pattern):
    win_start = 0
    c2freq = dict()
    res = []
    remains = len(pattern)
    for c in pattern:
        if c not in c2freq:
            c2freq[c] = 0
        c2freq[c] += 1

    for win_end, c in enumerate(str1):
        if c in c2freq:
            if c2freq[c] > 0:
                remains -= 1
            c2freq[c] -= 1

        if win_end >= len(pattern) - 1:
            if remains == 0:
                res.append(win_start)
            ch = str1[win_start]
            if ch in c2freq:
                if c2freq[ch] >= 0:
                    remains += 1
                c2freq[ch] += 1
        
            win_start += 1

    return res


def main():
    print(find_string_anagrams("ppqp", "pq"))  # [1, 2]
    print(find_string_anagrams("abbcabc", "abc"))  # [2, 3, 4]


main()


"""
Time O(N + M)
Space O(N): space to store result
"""

