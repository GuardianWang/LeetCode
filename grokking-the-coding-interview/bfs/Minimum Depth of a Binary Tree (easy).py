"""
LC 111
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
    if not root:
        return 0
    res = 0
    level = deque([root])
    while level:
        res += 1
        for _ in range(len(level)):
            n = level.popleft()
            # return at the first leaf
            if not n.left and not n.right:
                return res 
            if n.left:
              level.append(n.left)
            if n.right
              level.append(n.right)


def main():
  # 2 3
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()


"""
Time O(N)
Space O(N)
"""

