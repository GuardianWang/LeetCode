"""
https://leetcode.com/playground/SRN4cLVP

"""
from itertools import *


def minDist(s):
    d = 0
    for a, b in pairwise(chain('A', s)):
        d += pair_dist(a, b)
    return d
        
        
def pair_dist(a, b):
    d = (ord(a) - ord(b)) % 26
    return min(d, 26 - d)


s = "AZGB"  # 13
print(minDist(s))
s = 'ZNMD'  # 23
print(minDist(s))


"""
Time O(N)
Space O(1)
"""
