"""
LC 637
Given a binary tree, populate an array to represent the averages of all of its levels.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  if not root:
    return []
  res = []
  level = deque([root])
  while level:
    res.append(sum([node.val for node in level]) / len(level))
    for _ in range(len(level)):
      node = level.popleft()
      if node.left:
        level.append(node.left)
      if node.right:
        level.append(node.right)

  return res


def main():
  # [12.0, 4.0, 6.5]
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()


"""
Time O(N)
Space O(N): number of leaves
"""

