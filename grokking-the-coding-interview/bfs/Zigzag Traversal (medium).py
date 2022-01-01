"""
LC 103
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
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
    level = deque([root])
    reverse = False
    while level:
        if not reverse:
            res.append([node.val for node in level])
        else:
            res.append([node.val for node in reversed(level)])
        reverse = not reverse
        for _ in range(len(level)):
            node = level.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
    return res


def main():
  # [[12], [1, 7], [9, 10, 5], [17, 20]]
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()

