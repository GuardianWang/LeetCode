"""
LC 102
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    res = []

    level = deque([root])
    while level:
        res.append([n.val for n in level])
        for _ in range(len(level)):
            node = level.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
    return res


def main():
    # [[12], [7, 1], [9, 10, 5]]
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()


"""
Space O(N)
Time O(N)
"""

