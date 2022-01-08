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
    exprs = deque([(nums, ops)])
    for _ in range(len(ops)):
        for _ in range(len(exprs)):
            ex_nums, ex_ops = exprs.popleft()
            # calculation order
            for i in range(len(ex_ops)):
                # use ops[i] and 
                # nums[i], nums[i + 1] 
                new_num = str(eval("".join([ex_nums[i], ex_ops[i], ex_nums[i + 1]])))
                if len(ex_ops) == 1:
                    # last iteration
                    exprs.append(int(new_num))
                else:
                    new_nums, new_ops = [], []
                    new_nums.extend(ex_nums[:i])
                    new_nums.append(new_num)
                    new_nums.extend(ex_nums[i + 2:])
                    new_ops.extend(ex_ops[:i])
                    new_ops.extend(ex_ops[i + 1:])
                    exprs.append((new_nums, new_ops))

    return exprs


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()


"""
Time/Space O(N*(N-1)!) = O(N!)
"""

