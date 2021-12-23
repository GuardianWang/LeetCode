"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""


def search_triplets(arr):
    if len(arr) < 3:
        return []
    arr.sort()
    res = []
    # skip duplicated value
    last_n1 = float('inf')
    for i in range(len(arr) - 2):
        if arr[i] == last_n1:
            continue
        else:
            last_n1 = arr[i]

        j, k = i + 1, len(arr) - 1
        while j < k:

            s = arr[j] + arr[k]
            if s < -arr[i]:
                while j < k and arr[j] == arr[j + 1]:
                    j += 1
                j += 1
            elif s > -arr[i]:
                while j < k and arr[k] == arr[k - 1]:
                    k -= 1
                k -= 1
            else:
                res.append([arr[i], arr[j], arr[k]])
                while j < k and arr[j] == arr[j + 1]:
                    j += 1
                j += 1
                while j < k and arr[k] == arr[k - 1]:
                    k -= 1
                k -= 1
    return res


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()


"""
Time O(N^2)
Space O(N^2) for output and O(N) for sorting
"""

