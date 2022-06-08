"""
LC 269
There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters. Write a method to find the correct order of characters in the alien language.
Example 1:
Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

From the above two points, we can conclude that the correct character order is: "bac"
Example 2:
Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

From the above two points, we can conclude that the correct character order is: "cab"
Example 3:
Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

From the above five points, we can conclude that the correct character order is: "ywxz"
"""
from collections import defaultdict


def find_order(words):
    chars = set("".join(words))
    build = build_map(words)
    if not build:
        return ""
    node2children, node2in_deg = build
    if not node2in_deg:  # no rules learned
        return "".join(chars)
    vocab = [c for c in chars if c not in node2in_deg]
    ptr = 0
    while ptr < len(vocab):
        next_ptr = len(vocab)
        for i in range(ptr, next_ptr):
            node = vocab[i]
            for child in node2children[node]:
                node2in_deg[child] -= 1
                if node2in_deg[child] == 0:
                    vocab.append(child)
        ptr = next_ptr

    return "".join(vocab) if len(vocab) == len(chars) else ""


def build_map(words):
    node2children = defaultdict(list)
    node2in_deg = defaultdict(int)
    visited = set()
    for i in range(len(words) - 1):
        if len(words[i]) > len(words[i + 1]) and words[i][:len(words[i + 1])] == words[i + 1]:
            return False  # break the order
        for a, b in zip(words[i], words[i + 1]):
            if a == b:
                continue
            if (a, b) in visited:
                break  # a < b
            elif (b, a) in visited:
                return False  # break the order
            else:
                node2children[a].append(b)
                node2in_deg[b] += 1
                visited.add((a, b))
                break  # a < b
    return node2children, node2in_deg


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()


"""
Time O(N), N=#letters in words
Space O(1), alphabet <= 26
"""

