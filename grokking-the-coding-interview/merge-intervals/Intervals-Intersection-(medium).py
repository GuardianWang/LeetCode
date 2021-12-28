"""
LC 986
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""


def merge(intervals_a, intervals_b):
    l, r = 0, 1
    p1, p2 = 0, 0
    intersections = []
    while p1 < len(intervals_a) and p2 < len(intervals_b):
        i1, i2 = intervals_a[p1], intervals_b[p2]
        if is_overlap(i1, i2):
            intersections.append(intersect(i1, i2))

        # possible intersection happens in between [min(i1[r], i2[r]), max(i1[r], i2[r])]
        # so move to the next by min(i1[r], i2[r])
        if i1[r] < i2[r]:
            p1 += 1
        else:
            p2 += 1

    return intersections
    

def is_overlap(i1, i2):
    l, r = 0, 1
    return (i2[l] <= i1[l] <= i2[r]) or (i1[l] <= i2[l] <= i1[r])


def intersect(i1, i2):
    return [max(i1[0], i2[0]), min(i1[1], i2[1])]


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[3, 4]])))  # [[3, 3]]


main()


"""
Time O(M+N)
Space O(M+N)
"""

