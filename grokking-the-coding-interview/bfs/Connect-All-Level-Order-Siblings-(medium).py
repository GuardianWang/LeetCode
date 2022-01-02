"""
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
    if root is None:
        return
    start = root
    last_level_end = root
    while start:
        it = iter_level(start)
        prev = next(it, None)
        next_start = prev
        sibling = None
        for sibling in it:
            prev.next = sibling
            prev = sibling
        last_level_end.next = next_start
        start = next_start
        last_level_end = prev
    return root


def iter_level(start):
    while start:
        if start.left:
            yield start.left
        if start.right:
            yield start.right
        start = start.next


def main():
  # 12 7 1 9 10 5
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()


"""
Time O(N)
Space O(1)
"""
