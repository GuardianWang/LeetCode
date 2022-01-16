"""
LC 605
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        # first plantable
        pos = self.next_pos(flowerbed, 0)
         
        while n:
            if 0 <= pos < len(flowerbed):
                flowerbed[pos] = 1
                n -= 1
                pos = self.next_pos(flowerbed, pos)
            else:
                return False
        return True

    def next_pos(self, flowerbed, pos):
        while pos < len(flowerbed):
            if self.can_place(flowerbed, pos):
                break
            pos += 1
        return pos
            
    def can_place(self, flowerbed, i):
        if flowerbed[i]:
            return False

        left_avail = True 
        if i - 1 >= 0:
            left_avail = flowerbed[i - 1] == 0
        right_avail = True 
        if i + 1 < len(flowerbed):
            right_avail = flowerbed[i + 1] == 0
        return left_avail and right_avail


"""
Time O(N)
Space O(1)
"""

