"""
LC 46
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""
from collections import deque


def find_permutations(nums):
    res = deque([[]])
    for i, n in enumerate(nums):
        for _ in range(len(res)):
            x = res.popleft()
            for j in range(i + 1):
                res.append(x.copy())
                res[-1].insert(j, n)
    
    return list(res)


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()



"""
Time/Space O(N*N!)
"""

