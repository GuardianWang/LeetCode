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
