"""
LC 18
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""


def search_quadruplets(arr, target):
    res = []
    arr.sort()
    last_n1 = None
    for i in range(len(arr) - 3):
        if arr[i] > target / 4:
            break
        if arr[i] == last_n1:
            continue
        last_n1 = arr[i]
        last_n2 = None
        for j in range(i + 1, len(arr) - 2):
            if arr[j] > (target - arr[i]) / 3:
                break
            if arr[j] == last_n2:
                continue
            last_n2 = arr[j]

            l, r = j + 1, len(arr) - 1
            while l < r:
                if arr[l] > (target - arr[i] - arr[j]) / 2:
                    break
                quad = [arr[x] for x in [i, j, l, r]]
                s = sum(quad)
                if s == target:
                    res.append(quad)
                    while l < r and arr[l] == arr[l + 1]:
                        l += 1
                    l += 1
                    while l < r and arr[r - 1] == arr[r]:
                        r -= 1
                    r -= 1
                elif s < target:
                    while l < r and arr[l] == arr[l + 1]:
                        l += 1
                    l += 1
                else:
                    while l < r and arr[r - 1] == arr[r]:
                        r -= 1
                    r -= 1
    return res


def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()


"""
Time O(N^3)
Space O(N) sort, O(N^3) output
"""

