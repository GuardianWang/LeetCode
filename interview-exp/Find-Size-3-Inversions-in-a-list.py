"""
https://leetcode.com/playground/BZSXnYCA

Inversion is a strictly decreasing subsequence of length 3. More formally, given an array, p, an inversion in the array is any time some p[i] > p[j] > p[k] and i < j < k. Given an array of length n, find the number of inversions.

Example)
n = 5, arr = [5, 3, 4, 2, 1]
Array inversions are [5, 3, 2], [5,3,1], [5,4,2], [5,4,1], [5,2,1], [3,2,1], [4,2,1]

n = 4, arr = [4,2,2,1]
The only inversion is [4,2,1] and we do not count the duplicate inversion.
"""
def find_inv2(l):
    sorted_unique_values = sorted(set(l))
    # BIT index starts from 1
    v2treeid = {v: i + 1 for i, v in enumerate(sorted_unique_values)}
    def update(v):
        treeid = v2treeid[v]
        while treeid < len(bit):
            # number of unique values
            bit[treeid] += 1
            treeid += treeid & -treeid
    
    def query(v):
        treeid = v2treeid[v]
        ans = 0
        while treeid > 0:
            # number of unique values
            ans += bit[treeid]
            treeid -= treeid & -treeid
        return ans
    
    # unique smaller values on the right
    smaller_right = [0] * len(l)
    bit = [0] * (len(sorted_unique_values) + 1)
    visited = set()
    for i in reversed(range(len(l))):
        v = l[i]
        if v not in visited:
            update(v)
        visited.add(v)
        
        if v != sorted_unique_values[0]:
            # smallest value has count = 0
            # query the nearest value smaller than v
            smaller_right[i] = query(sorted_unique_values[v2treeid[v] - 1 - 1]) 
    print(smaller_right)
    
    # unique larger values on the left
    larger_left = [0] * len(l)
    bit = [0] * (len(sorted_unique_values) + 1)
    visited = set()
    for i, n in enumerate(l):
        v = l[i]
        if v not in visited:
            update(v)
        visited.add(v)
        
        if v != sorted_unique_values[-1]:
            # largest value has count = 0
            larger_left[i] = query(sorted_unique_values[-1]) - query(sorted_unique_values[v2treeid[v] - 1])  
    print(larger_left)
    
    # unique triplet
    visited2largeleft = {}
    cnt = 0
    for i, (v, n_large, n_small) in enumerate(zip(l, larger_left, smaller_right)):
        if v in visited2largeleft:
            # compared with the last occurrence, the new encountered larger value on the left
            # paired with the smaller values on the right make up of new triplets
            cnt += (n_large - visited2largeleft[v]) * n_small
        else:
            cnt += n_large * n_small
        visited2largeleft[v] = n_large
    
    return cnt


"""
Time O(NlogN)
Space O(N)
"""
 