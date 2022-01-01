"""
LC 199
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
    if not root:
        return []
    res = []
    level = deque([root])
    while level:
        l = len(level)
        for i in range(l):
            n = level.popleft()
            if i == l - 1:
                res.append(n)
            if n.left:
                level.append(n.left)
            if n.right:
                level.append(n.right)
    return res


def main():
  # 12 1 5 3
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()


"""
Time O(N)
Space O(N)
"""

