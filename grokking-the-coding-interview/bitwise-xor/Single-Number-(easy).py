"""
LC 136
In a non-empty array of integers, every number appears twice except for one, find that single number.
Example 1:
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:
Input: 7, 9, 7
Output: 9
"""
def find_single_number(arr):
    m = 0
    for n in arr:
        m ^= n
    return m


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()


"""
Time O(N)
Space O(1)
"""
