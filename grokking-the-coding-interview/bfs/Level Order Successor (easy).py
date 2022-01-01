"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
    if not root:
        return None
    level = deque([root])
    while level:
        n = level.popleft()
        if n.left:
            level.append(n.left)
        if n.right:
            level.append(n.right)
        # 1. if right is on the same level, 
        # right has been enqueued 
        # 2. if right is on the beginning of next level,
        # right has been enqueued because node is the last of 
        # the current level
        if n.val == key:
            return level.popleft()


def main():
    # 7 10
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()


"""
Time O(N)
Space O(N)
"""

