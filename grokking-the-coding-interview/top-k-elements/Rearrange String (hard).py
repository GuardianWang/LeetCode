"""
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
from heapq import *


def rearrange_string(s):
  # count
  freqs = {}
  for c in s:
    if c in freqs:
      freqs[c] += 1
    else:
      freqs[c] = 1
  # arrange
  # max heap, first deal with letters that often appears
  h = [[-f, c] for c, f in freqs.items()]
  heapify(h)
  res = []
  prev = None
  for _ in range(len(s)):
      if not h:
          return ""

      top = heappop(h)
      res.append(top[1])
      top[0] += 1

      if prev:
          heappush(h, prev)
      prev = top
      if 0 == prev[0]:
          prev = None


  return "".join(res)


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()


"""
#letters is O(1)
Time O(N)
Space O(1)
"""
