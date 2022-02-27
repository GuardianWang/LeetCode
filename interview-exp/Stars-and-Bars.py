"""
https://leetcode.com/playground/C3bVUrWS

Given a string s consisting of stars "*" and bars "| ", an array of starting indices startindex, and an
array of ending indices endindex, determine the number of stars between any two bars within
the substring between the two indices, inclusive. Note that in this problem, indexing starts at 1.
. A star is represented as an asterisk (* = ascii decimal 42)
. A bar is represented as a pipe (|' = ascii decimal 124).

Example
startindex = [1, 1]
endIndex = [5, 6]

For the first pair of indices, (1, 5), the substring is ' | ** |*. There are 2 stars between a pair of
bars.
For the second pair of indices, (1, 6), the substring is ' |**|* |' and there are 2 + 1 =3 stars
between bars.
Both of the answers are returned in an array, [2, 3].
"""
from itertools import *
from bisect import *

def cnt(s, l, r):
    # 0-indexed
    l -= 1
    r -= 1
    # binary index tree
    # s = '|**|*|*'
    # star_cnt = [2, 1, 1]
    # bar_idx = [0, 3, 5]
    
    def update(idx, v):
        while idx < len(bit):
            bit[idx] += v
            idx += idx & -idx
    
    def query(idx):
        ans = 0
        while idx > 0:
            ans += bit[idx]
            idx -= idx & -idx
        return ans
    
    # preprocess
    bar_idx = [i for i, c in enumerate(s) if c == '|']
    star_cnt = [r_bar - l_bar - 1 for l_bar, r_bar in pairwise(bar_idx)]
        
    # build BIT
    bit = [0] * (1 + len(star_cnt))
    for i, cnt in enumerate(star_cnt, 1):
        update(i, cnt)
        
    # query
    l = min(bisect_left(bar_idx, l), len(bar_idx) - 1)  # closest index >= l
    r = max(bisect_right(bar_idx, r) - 1, 0)  # closest index <= r
    if l >= r:
        return 0
    else:
        return query(r) - query(l)
    

s = '|**|*|*'

print(cnt(s, 1, 6))


"""
Time O((N+Q)logN)
Space O(NlogN)
"""
