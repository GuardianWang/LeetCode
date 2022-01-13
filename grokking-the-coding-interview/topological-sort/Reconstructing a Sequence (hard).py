"""
LC 444
Given a sequence originalSeq and an array of sequences,
write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.
Unique reconstruction means that we need to find if originalSeq is the only sequence
such that all sequences in the array are subsequences of it.
Example 1:
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct
[1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers
in the 'originalSeq'.
Example 2:
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct
[1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]
Example 3:
Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct
[3, 1, 4, 2, 5].
"""
from collections import defaultdict


def can_construct(originalSeq, sequences):
    if len(set([y for x in sequences for y in x])) != len(originalSeq):
        return False
    node2children, node2in_deg = build_map(sequences)
    order = [[x for x in originalSeq if x not in node2in_deg]]
    while order[-1]:
        if len(order[-1]) > 1 or order[-1][0] != originalSeq[len(order) - 1]:
            return False
        next_group = []
        for child in node2children[order[-1][0]]:
            node2in_deg[child] -= 1
            if node2in_deg[child] == 0:
                next_group.append(child)
        order.append(next_group)
    if not order[-1]:
        order.pop()
    return len(order) == len(originalSeq)


def build_map(sequences):
    node2children = defaultdict(list)
    node2in_deg = defaultdict(int)
    for s in sequences:
        for i in range(len(s) - 1):
            node2children[s[i]].append(s[i + 1])
            node2in_deg[s[i + 1]] += 1
    return node2children, node2in_deg


def can_construct2(originalSeq, sequences):
    # dict
    # this is wrong because this cannot prove uniqueness
    if len(set([y for x in sequences for y in x])) != len(originalSeq):
        return False
    n2id = {n: i for i, n in enumerate(originalSeq)}
    for s in sequences:
        for i in range(len(s) - 1):
            if s[i] not in n2id or s[i + 1] not in n2id or n2id[s[i]] > n2id[s[i + 1]]:
                return False
    return True


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()


"""
Time O(V+E)
Space O(V+E)
"""

