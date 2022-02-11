"""
LC 2157
You are given a 0-indexed array of strings words. Each string consists of lowercase English letters only. No letter occurs more than once in any string of words.

Two strings s1 and s2 are said to be connected if the set of letters of s2 can be obtained from the set of letters of s1 by any one of the following operations:

Adding exactly one letter to the set of the letters of s1.
Deleting exactly one letter from the set of the letters of s1.
Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.
The array words can be divided into one or more non-intersecting groups. A string belongs to a group if any one of the following is true:

It is connected to at least one other string of the group.
It is the only string present in the group.
Note that the strings in words should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.

Return an array ans of size 2 where:

ans[0] is the total number of groups words can be divided into, and
ans[1] is the size of the largest group.
 

Example 1:

Input: words = ["a","b","ab","cde"]
Output: [2,3]
Explanation:
- words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].
- words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].
- words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1].
- words[3] is not connected to any string in words.
Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.  
Example 2:

Input: words = ["a","ab","abc"]
Output: [1,3]
Explanation:
- words[0] is connected to words[1].
- words[1] is connected to words[0] and words[2].
- words[2] is connected to words[1].
Since all strings are connected to each other, they should be grouped together.
Thus, the size of the largest group is 3.
"""
class Solution:
    def groupStrings(self, words):
        
        # represent letters with mask
        cnt_mask = defaultdict(int)
        for w in words:
            cnt_mask[self.get_mask(w)] += 1
        masks = list(cnt_mask.keys())
        visited = set()
        s = 0
        # for each mask, only add, only delete, or both
        def dfs(mask):
            if mask in visited or mask not in cnt_mask:
                return 0
            visited.add(mask)
            s = cnt_mask[mask]
            for i in range(26):
                if mask & (1 << i):
                    s += dfs(mask ^ (1 << i))  # delete
                    
                    for j in range(26):
                        if 0 == (mask & (1 << j)):
                            s += dfs(mask ^ (1 << i) | (1 << j))  # delete and add
                    
                else:
                    s += dfs(mask | 1 << i)  # add letter
            return s
        n_group, M = 0, 0
        for m in masks:
            s = dfs(m)
            if s:
                n_group += 1
                M = max(M, s)
        return n_group, M
    
    def get_mask(self, word):
        mask = 0
        word = set(word)
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        return mask
             

"""
Time O(N)
Space O(1)
"""
