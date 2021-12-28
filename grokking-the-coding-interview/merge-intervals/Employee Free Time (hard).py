"""
LC 759
For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: All the employees are free between [3,5].
Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].
Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7].
"""


from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):     
    heap = []
    # all working hours 
    work = [t for w in schedule for t in w]
    work.sort(key=lambda x: x.start)
    merge_work = [work[0]]
    for i in range(1, len(work)):
        if work[i].start <= merge_work[-1].end:
            merge_work[-1].end = max(merge_work[-1].end, work[i].end)
        else:
            merge_work.append(work[i])
    work = merge_work
    # rest 
    rest = [Interval(work[i - 1].end, work[i].start) for i in range(1, len(work)) 
            if work[i - 1].end < work[i].start]
    rest.sort(key=lambda x: x.start)
    # result
    res = [Interval(rest[0].start, rest[0].end)]
    for r in rest:
        heappush(heap, (r.end, r.start))
        if heap[0][0] <= r.start:
            while heap and heap[0][0] < r.start:
                heappop(heap)
            res.append(Interval(r.start, r.end))
        else:
            res[-1].start = max(r.start, res[-1].start)
            res[-1].end = heap[0][0]

    return res 


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()


"""
Time O(NlogN)
Space O(N)
"""

