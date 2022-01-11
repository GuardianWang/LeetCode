"""
LC 358
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.
Example 1:
Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.
Example 2:
Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
Explanation: All same characters are 3 distance apart.
Example 3:
Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.
Example 4:
Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
"""
from collections import deque
from heapq import *


def reorganize_string(s, k):
    if len(s) <= 1:
        return s
    if k <= 1:
        return s

    # count
    freqs = {}
    for c in s:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    freqs = [[-f, c, -1] for c, f in freqs.items()]
    heapify(freqs)  # max heap
    # rearrange
    prevs = deque()  # max size k - 1
    ans = []
    for i in range(len(s)):
        if not freqs:
            return ""

        top = heappop(freqs)
        ans.append(top[1])
        top[0] += 1
        if top[0]:
            top[2] = i  # last added at index i
            prevs.append(top)
        if prevs and i + 1 - prevs[0][2] >= k:  # far enough
            # i + 1 because need to consider the next iteration
            heappush(freqs, prevs.popleft())

    return "".join(ans)


def main():
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()


"""
#letters is O(1)
Time O(N)
Space O(1)
"""
