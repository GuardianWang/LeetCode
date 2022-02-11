"""
LC 1101
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 

Example 1:

Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friends anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
Example 2:

Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
"""
# union-find and group counter
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if len(logs) < n - 1:
            return -1
        logs.sort(key=lambda x: x[0])
        self.groups = list(range(n))
        self.ranks = [0] * n
        
        for t, a, b in logs:
            if self.union(a, b):
                n -= 1
            if n == 1:
                return t
            
        return -1
            
    def find(self, x):
        if self.groups[x] != x:
            self.groups[x] = self.find(self.groups[x])
        return self.groups[x]  # root
        
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # didn't merge
        if self.ranks[a] < self.ranks[b]:
            self.groups[ra] = rb
        elif self.ranks[b] < self.ranks[a]:
            self.groups[rb] = ra
        else:
            self.groups[ra] = rb
            self.ranks[rb] += 1
        return True


"""
Time O(N+MlogM)
Space O(N+M)
"""
