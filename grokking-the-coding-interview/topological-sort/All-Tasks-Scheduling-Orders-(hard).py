"""
LC 1916
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs,
write a method to print all possible ordering of tasks meeting all prerequisites.
Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
Example 2:
Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output:
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.
Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output:
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
"""
from collections import defaultdict, deque
from math import comb
from itertools import accumulate, chain
from operator import mul


def print_orders(tasks, prerequisites):
    node2children, node2parent, node2in_deg = build_map(prerequisites)
    ans = deque([[]])
    order = [[t for t in range(tasks) if t not in node2in_deg]]
    while order[-1]:
        new_group = []
        for node in order[-1]:
            for child in node2children[node]:
                node2in_deg[child] -= 1
                if node2in_deg[child] == 0:
                    new_group.append(child)
        order.append(new_group)
    order.pop()

    for subgroup in order:
        permute_subgroup(ans, subgroup, node2parent)
    if not ans[0]:
        ans.pop()
    print(ans)


def permute_subgroup(ans, nums, node2parent):
    for n in nums:
        for i in range(len(ans)):
            base = ans.popleft()
            # after the max index of all parents
            start = 0 if n not in node2parent else \
                max(map(lambda x: base.index(x), node2parent[n])) + 1
            for j in range(start, len(base) + 1):
                permu = base.copy()
                permu.insert(j, n)
                ans.append(permu)


def build_map(prerequisites):
    node2children = defaultdict(list)
    node2parent = defaultdict(list)
    node2in_deg = defaultdict(int)
    for from_node, to_node in prerequisites:
        node2parent[to_node].append(from_node)
        node2children[from_node].append(to_node)
        node2in_deg[to_node] += 1
    return node2children, node2parent, node2in_deg


def count_permutation(node2children, order, n):
    # https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/2120091/Python-10-lines-Post-Order-with-thought-process-when-being-asked-during-interviews
    mod = int(1e9 + 7)
    factorial = list(chain([1], accumulate(range(1, n + 1), lambda x, y: mul(x, y) % mod)))
    factorial_inv = chain([pow(factorial[-1], mod - 2, mod)], reversed(range(1, n + 1)))
    factorial_inv = list(accumulate(factorial_inv, lambda x, y: mul(x, y) % mod))
    factorial_inv.reverse()

    # applicable when one node has only 1 parent (tree)
    dp = [1] * n
    sz = dp.copy()
    for i in range(-2, -len(order) - 1, -1):
        # in the same subgroup, one is not the other's child
        for node in order[i]:
            init_sz = 0
            for child in node2children[node]:
                # multinomial distribution
                # sum(nums)!/(n1!n2!...) =
                # comb(n1, n1) * comb(sum(nums[:2]), n2) * ...
                init_sz += sz[child]
                dp[node] *= dp[child] * factorial_inv[sz[child]]
                dp[node] %= mod
            dp[node] *= factorial[init_sz]
            dp[node] %= mod
            sz[node] += init_sz
    return dp[0]


def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])

  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2], [2, 0]])


main()


"""
Time/Space O(V!V+E)
"""
