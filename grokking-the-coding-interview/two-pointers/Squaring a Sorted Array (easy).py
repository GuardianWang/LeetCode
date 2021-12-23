"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""

def make_squares(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr[0] ** 2]

    # min abs value
    min_id = 0
    min_val = float('inf')
    for i, v in enumerate(arr):
        if abs(v) < min_val:
            min_id = i
            min_val = abs(v) 
        if i > 0 and abs(arr[i - 1]) <= v:
            break

    # two pointers
    if min_id == len(arr) - 1:  
        l, r = min_id - 1, min_id
    elif min_id == 0:
        l, r = min_id, min_id + 1
    elif abs(arr[min_id - 1]) < abs(arr[min_id + 1]):
        l, r = min_id - 1, min_id
    else:
        l, r = min_id, min_id + 1

    # construct result
    res = []
    while l >= 0 or r < len(arr):
        if r >= len(arr) or abs(arr[l]) < abs(arr[r]):
            res.append(arr[l] ** 2)
            l -= 1
        else:
            res.append(arr[r] ** 2)
            r += 1
    return res


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()


"""
Time O(N)
Space O(1)
"""

