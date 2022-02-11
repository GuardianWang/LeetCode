"""
LC 1274
Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example :


Input:
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
Example 2:

Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
Output: 3
"""
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        self.cnt = 0
        self.sea = sea
        self.dfs(topRight, bottomLeft)
        return self.cnt

    def dfs(self, topRight, bottomLeft):
        if not self.hasShips(topRight, bottomLeft):
            return
        mid_x = (topRight.x + bottomLeft.x) >> 1
        mid_y = (topRight.y + bottomLeft.y) >> 1

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            self.cnt += 1
        elif topRight.x == bottomLeft.x:
            self.dfs(topRight, Point(topRight.x, mid_y + 1))
            self.dfs(Point(topRight.x, mid_y), bottomLeft)
        elif topRight.y == bottomLeft.y:
            self.dfs(topRight, Point(mid_x + 1, topRight.y))
            self.dfs(Point(mid_x, topRight.y), bottomLeft)
        else:
            self.dfs(topRight, Point(mid_x + 1, mid_y + 1))
            self.dfs(Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
            self.dfs(Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
            self.dfs(Point(mid_x, mid_y), bottomLeft)

    def hasShips(self, topRight, bottomLeft):
        return self.sea.hasShips(topRight, bottomLeft)


"""
Time O(SlogN): logN to find each ship
Space O(logN): balanced tree
"""
