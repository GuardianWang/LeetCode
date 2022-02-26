"""
https://leetcode.com/playground/BZSXnYCA

Inversion is a strictly decreasing subsequence of length 3. More formally, given an array, p, an inversion in the array is any time some p[i] > p[j] > p[k] and i < j < k. Given an array of length n, find the number of inversions.

Example)
n = 5, arr = [5, 3, 4, 2, 1]
Array inversions are [5, 3, 2], [5,3,1], [5,4,2], [5,4,1], [5,2,1], [3,2,1], [4,2,1]

n = 4, arr = [4,2,2,1]
The only inversion is [4,2,1] and we do not count the duplicate inversion.
"""
def find_inv1(l):
    # count number of unique smaller values on the right
    cnt_small_right = [0] * len(l)
    for i in range(len(l)):
        visited = set()
        for j in range(i + 1, len(l)):
            if l[j] in visited:
                continue
            visited.add(l[j])
            if l[j] < l[i]:
                cnt_small_right[i] += 1

    # count triplet
    visited = set()
    ans = 0
    for i in range(len(l)):
        if l[i] in visited:
            continue
        visited.add(l[i])
        visited2 = set()
        for j in range(i + 1, len(l)):
            if l[j] in visited2 or l[i] <= l[j]:
                continue
            visited2.add(l[j])
            ans += cnt_small_right[j]
    return ans


"""
Time O(N^2)
Space O(N)
"""
