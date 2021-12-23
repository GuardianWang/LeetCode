"""
LC 30
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""


def find_word_concatenation(str1, words):
    remains = len(words)
    w_len = len(words[0])
    sum_len = remains * w_len
    w2freq = dict()
    for w in words:
        if w not in w2freq:
            w2freq[w] = 0
        w2freq[w] += 1


    res = []
    for win_start, win_end in enumerate(range(sum_len - 1, len(str1))):
        w2freq_copy = w2freq.copy()
        for l in range(win_start, win_end, 3):
            r = l + 3
            w = str1[l: r]
            if w in w2freq_copy:
                if w2freq_copy[w] == 0:
                    break
                else:
                    w2freq_copy[w] -= 1
            else:
                break
        else:
            res.append(win_start)
    return res


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))  # [0, 3]
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))  # [3]


main()


"""
Time O(NML)
Space O(N+ML): N for result
"""

