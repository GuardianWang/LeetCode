"""
LC 117
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
    if root is None:
        return None 
    # because we can use .next to traverse each level 
    # space can be O(1)
    start = root 
    while start:
      # connect the next level 
      next_iter = iter_next_level(start)
      prev = next(next_iter, None)
      next_start = prev
      for sibling in next_iter:
        prev.next = sibling 
        prev = sibling 
      start = next_start


def iter_next_level(start):
  while start:
    if start.left:
      yield start.left 
    if start.right:
      yield start.right
    start = start.next 


def main():
  # 12 
  # 7 1 
  # 9 10 5 
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()


"""
Time O(N)
Space O(1)
"""

