"""
https://leetcode.com/playground/QarZVLpM

Given tiles of dimensions 1 x 1 x 2, determine how many ways they can be arranged to form a
rectangular solid of dimensions 2 x 2 x n.
For example, if n = 1, there are two ways of doing so:

The number of permutations increases quickly, so the return value should be modulo (109+7).
See the samples below for the n = 2 solution diagrams.
Function Description
Complete the function ways in the editor below. The function should return an array of integers
that represent the number of ways each solid can be formed.
"""
def count3d(n):
    if n == 1:
        return 2
    
    MOD = int(1e9 + 7)

    # full
    # f(n) = 2 * f(n - 1) + 5 * f(n - 2) + 4 * p(n - 1)
    # 2: vertical + horizontal
    # 5: all vertical + 4 * (2 ver, 2 hor)
    # 4: (1 hor), 4 orientations
    # cannot use 4 * p(n) because there are overlaps between f(n - 2)
    f = [1, 2]
    
    # partial, one orientation, top layer is vertical
    # p(n) = f(n - 2) + p(n - 1)
    p = 0  # p(1)
    
    for _ in range(n - 1):
        f, p = [f[1], (5 * f[0] + 2 * f[1] + 4 * p) % MOD], (p + f[0]) % MOD

    return f[1]
    
                
print(count3d(100))  # 828630254


"""
Time O(N)
Space O(1)
"""
