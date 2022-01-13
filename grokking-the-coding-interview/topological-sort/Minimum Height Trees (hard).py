"""
LC 310
We are given an undirected graph that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.
Example 1:
Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the
height of the trees with roots '1' or '2' is three which is minimum.
"""
from collections import defaultdict


def find_trees(nodes, edges):
    node2children = build_map(edges)
    while len(node2children) > 2:
        remove_leaves(node2children)
    return list(node2children.keys())


def build_map(edges):
    node2children = defaultdict(set)
    for i, o in edges:
        node2children[i].add(o)
        node2children[o].add(i)
    return node2children


def remove_leaves(node2children):
    leaves = [k for k, v in node2children.items() if len(v) == 1]
    for leaf in leaves:
        node2children[node2children[leaf].pop()].remove(leaf)
        del node2children[leaf]


def main():
  # [1, 2] [0, 2] [1]
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()


"""
Time O(V^2): find new leaves
Space O(V): it's a tree
"""
