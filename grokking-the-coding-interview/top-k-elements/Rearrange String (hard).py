"""
LC 767
Given a string, find if its letters can be rearranged in such a way that no two same characters ome next to each other.
Example 1:
Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.
Example 2:
Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:
Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
"""
from collections import Counter


def rearrange_string(s):
  # count
  freqs = Counter(s)
  # arrange
  res = [''] * len(s)
  l = 0  # next start
  for c, f in freqs.most_common(len(freqs)):
    # fill in either odd or even pos
    if l + 2 * (f - 1) >= len(s):  # out of range
      return ""
    r = l
    for _ in range(f):
      if res[l] and r > 0 and not res[r - 1]:
        l = r - 1  # update next start
      res[r] = c
      r += 2
    if res[l]:  # update next start
      l = r - 2
      while l < len(s) and res[l]:
        l += 1

  return "".join(res)


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()
