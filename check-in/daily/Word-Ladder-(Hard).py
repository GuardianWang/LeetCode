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
        wordList.append(beginWord)
        wordList = set(wordList)
        self.word_set = wordList

        level = deque([beginWord])
        cnt = 1

        while level:
            cnt += 1
            for _ in range(len(level)):
                for c in self.n2c(level.popleft()):
                    if c == endWord:
                        return cnt
                    level.append(c)

        return 0

    def n2c(self, s1):
        for i in range(len(s1)):
            for k in map(chr, range(ord('a'), ord('z') + 1)):
                if k == s1[i]:
                    continue
                s2 = s1[:i] + k + s1[i + 1:]
                if s2 not in self.word_set:
                    continue
                self.word_set.remove(s2)
                yield s2


"""
Time O(L^2 * N)
Space O(LN)
"""
