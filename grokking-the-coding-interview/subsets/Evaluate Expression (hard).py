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
    # dp to save time for recursion
    # bottom-up
    # dp[a][b] is all possible values from the a-th number to the b-th number 
    dp = [[[] for _ in range(len(nums))] for _ in range(len(nums))]
    # init dp[n][n]
    for i, num in enumerate(nums):
        dp[i][i].append(num)
    for step in range(1, len(nums)):
        for i in range(len(nums) - step):
            j = i + step 
            for m in range(i, j):
                dp[i][j].extend(calculate(dp[i][m], dp[m + 1][j], ops[m])) 

    return list(map(int, dp[0][len(nums) - 1]))


def calculate(values_l, values_r, op):
    return [str(eval("".join([x, op, y]))) for x in values_l for y in values_r]


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()


"""
Time/Space Catalan(N)
"""
