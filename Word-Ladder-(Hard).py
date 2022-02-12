"""
LC 127
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        word_set = set(wordList)
        n2c = defaultdict(set)
        for s1 in wordList:
            for i in range(len(s1)):
                for k in map(chr, range(ord('a'), ord('z') + 1)):
                    if k == s1[i]:
                        continue
                    s2 = s1[:i] + k + s1[i + 1:]
                    if s2 not in word_set:
                        continue
                    # at most 260 neighbors
                    n2c[s1].add(s2)
                    n2c[s2].add(s1)

        # bi-directional bfs
        n = beginWord
        vis = set([n])
        cnt = 1

        n2 = endWord
        vis2 = set([n2])
        cnt2 = 0

        level = deque([n])
        level2 = deque([n2])

        while level and level2:
            cnt += 1
            for _ in range(len(level)):
                n = level.popleft()
                for c in n2c[n]:
                    if c in vis:
                        continue
                    if c in vis2:
                        return cnt + cnt2
                    level.append(c)
                    vis.add(c)

            cnt2 += 1
            for _ in range(len(level2)):
                n = level2.popleft()
                for c in n2c[n]:
                    if c in vis2:
                        continue
                    if c in vis:
                        return cnt + cnt2
                    level2.append(c)
                    vis2.add(c)

        return 0


"""
Time/Space O(L^2 * N)
"""
