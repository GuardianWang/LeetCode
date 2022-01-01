"""
LC 104
Given a binary tree, find its maximum depth (or height).
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_maximum_depth(root):
  if not root:
    return 0 
  res = 0 
  level = deque([root])
  while level:
    res += 1 
    for _ in range(len(level)):
      n = level.popleft()
      if n.left:
        level.append(n.left)
      if n.right:
        level.append(n.right)
  return res


def main():
  # 3 4
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()


"""
Time O(N)
Space O(N)
"""

