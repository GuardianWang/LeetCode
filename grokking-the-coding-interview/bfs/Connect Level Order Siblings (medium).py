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
    level = deque([root])
    while level:
        l = len(level)
        for i in range(l):
            n = level.popleft()
            if i != l - 1:
                n.next = level[0]
            if n.left:
                level.append(n.left)
            if n.right:
                level.append(n.right)
    return root
    

def main():
  # 13 
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
Space O(N)
"""

