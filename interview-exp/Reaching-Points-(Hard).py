"""
LC 780
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

 

Example 1:

Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
Example 2:

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
Example 3:

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx:
                return (ty - sy) % sx == 0
            if ty == sy:
                return (tx - sx) % sy == 0
            
            if tx > ty:
                tx %= ty  # subtract until tx < ty
            elif tx < ty:
                ty %= tx
            else:
                # tx != sx or ty != sy
                return False
            
        return False
        
        
"""
Time O(log(max(tx, ty)))
Space O(1)
"""
