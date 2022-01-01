"""
Find the largest value on each level of a binary tree.
"""


from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_max(root):
    if not root:
        return []
    res = []
    level = deque([root])
    while level:
        res.append(max([n.val for n in level]))
        for _ in range(len(level)):
            n = level.popleft()
            if n.left:
                level.append(n.left)
            if n.right:
                level.append(n.right)
    return res


def main():
  # [12, 7, 10]
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_max(root)))


main()


"""
Time O(N)
Space O(N)
"""

