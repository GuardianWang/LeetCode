"""
LC 904
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
LC 904
"""
from collections import defaultdict


def fruits_into_baskets(fruits):
    if len(set(fruits)) <= 2:
        return len(fruits)
    
    max_len = 0
    l = 0
    f2cnt = defaultdict(int)
    
    for r, v in enumerate(fruits):
        f2cnt[v] += 1
        if len(f2cnt) > 2:
            lv = fruits[l]
            f2cnt[lv] -= 1
            l += 1
            if f2cnt[lv] == 0:
                del f2cnt[lv]
        else:
            max_len = max(max_len, r - l + 1)
    return max_len


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))  # 3
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))  # 5


main()


"""
Time O(N)
Space O(1)
"""