"""
https://leetcode.com/playground/2XVugSV5

Given binary String str and an integer k, find the lexicographically smallest and largest substring of length k with n '1's
"""
def min_max(s, k, n):
    # k: length of substring
    # n: number of 1
    M = m = s[:k]
    for sub_s in generate_sub(s, k, n):
        M = max(M, sub_s)
        m = min(m, sub_s)
    return M, m
        
    
def generate_sub(s, k, n):
    cnt = 0  # counter for 1
    for i in range(len(s) - k + 1):
        sub_s = s[i: i + k]
        if i == 0:
            cnt = sub_s.count('1')
        elif sub_s[-1] == '1':
            cnt += 1 
        
        if cnt == n:
            yield sub_s
        if sub_s[0] == '1':
            cnt -= 1
    
    
s = '101110'
print(min_max(s, 3, 2))


"""
Time O(LK)
Space O(K)
"""
