"""
LC 241
Given an expression containing digits and operations (+, -, *),
find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.
Example 1:
Input: "1+2*3"
Output: 7, 9
Explanation: 1+(2*3) => 7 and (1+2)*3 => 9
Example 2:
Input: "2*3-4-5"
Output: 8, -12, 7, -7, -3
Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3
"""
import re
from collections import deque


def diff_ways_to_evaluate_expression(expr):
    nums = re.findall(r"\d+", expr)
    ops = re.findall(r"\+|\-|\*", expr)
    return list(map(int, find_expr(nums, ops)))


def find_expr(nums, ops):
    # dfs
    if not ops:
        return nums

    values = []
    for i in range(len(ops)):
        values_l = find_expr(nums[:i + 1], ops[:i])
        values_r = find_expr(nums[i + 1:], ops[i + 1:])
        values.extend(calculate(values_l, values_r, ops[i]))
    return values


def calculate(values_l, values_r, op):
    return [str(eval("".join([x, op, y]))) for x in values_l for y in values_r]


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()


"""
Time/Space > O(3^N), maybe O(N!)
"""
