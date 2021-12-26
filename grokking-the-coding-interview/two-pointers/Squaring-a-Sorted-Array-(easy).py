"""
LC 977
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""

def make_squares(arr):
    if len(arr) == 1:
        return [arr[0] ** 2]
    
    # from max to min
    res = [0 for _ in arr]
    l, r = 0, len(arr) - 1
    p_place = r
    while l <= r:
        if abs(arr[l]) < abs(arr[r]):
            res[p_place] = arr[r] ** 2
            p_place -= 1
            r -= 1
        else:
            res[p_place] = arr[l] ** 2
            p_place -= 1
            l += 1
    return res 


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()


"""
Time O(N)
Space O(N)
"""

