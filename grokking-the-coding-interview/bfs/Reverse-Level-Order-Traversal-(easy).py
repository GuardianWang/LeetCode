"""
LC 107
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  if not root:
    return []

  res = []
  levels = [[root]]
  # traverse all
  while levels[-1]:
    levels.append([])
    for node in levels[-2]:  # now it's -2
      if node.left:
        levels[-1].append(node.left)
      if node.right:
        levels[-1].append(node.right)
  # backward 
  levels.pop()
  while levels:
    nodes = levels.pop()
    res.append([node.val for node in nodes])

  return res
    

def main():
  # [[9, 10, 5], [7, 1], [12]]
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()


"""
Time O(N)
Space O(N)
"""

