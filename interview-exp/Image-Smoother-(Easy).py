"""
LC 661
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
Can use highest bits to store value

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

 

Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        nr, nc = len(img), len(img[0])
        # decompose 
        # row
        for r in range(nr):
            window = deque([0, img[r][0]], 3)
            for c in range(1, nc + 1):
                if c < nc:
                    window.append(img[r][c])
                else:
                    window.append(0)
                img[r][c - 1] = sum(window)
        # column                
        for c in range(nc):
            window = deque([0, img[0][c]], 3)
            for r in range(1, nr + 1):
                if r < nr:
                    window.append(img[r][c])
                else:
                    window.append(0)
                img[r - 1][c] = sum(window)
        # average
        corner_denom = min(2, nr) * min(2, nc)
        col_edge_demon = 3 * min(2, nc)
        row_edge_demon = 3 * min(2, nr)
        for r, c in product(range(nr), range(nc)):
            between_td, between_lr = 0 < r < nr - 1, 0 < c < nc - 1
            if between_td and between_lr:
                # inner
                img[r][c] //= 9
            elif between_td:
                # column edge
                img[r][c] //= col_edge_demon
            elif between_lr:
                # row edge
                img[r][c] //= row_edge_demon
            else:
                # corner
                img[r][c] //= corner_denom
            
        return img


"""
Time O(MN)
Space O(1)
"""
