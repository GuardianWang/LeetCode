"""
LC 95
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
"""
from copy import deepcopy
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_unique_trees(n):
    dp = [[] for _ in range(n + 1)]
    dp[0] = [None]
    dp[1] = [TreeNode(1)]
    for i in range(2, n + 1):
        for j in range(i):
            build_trees(j + 1, dp[j], dp[i - 1 - j], dp[i])
        for node in dp[i]:
            renumber(node.right, node.val)
    return dp[-1]


def build_trees(val, lefts, rights, res):
    for l in lefts:
        for r in rights:
            root = TreeNode(val)
            root.left, root.right = deepcopy(l), deepcopy(r)
            res.append(root)
    return res


def renumber(root, delta):
    if not root:
        return
    nodes = deque([root])
    while nodes:
        node = nodes.popleft()
        node.val += delta
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)


def main():
  # 2 5 14 42
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))
  print("Total trees: " + str(len(find_unique_trees(4))))
  print("Total trees: " + str(len(find_unique_trees(5))))


main()


"""
Time/Space O(N * Catalan(N))
"""
