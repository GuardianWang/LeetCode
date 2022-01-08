"""
LC 22
Problem Statement
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
Example 1:
Input: N=2
Output: (()), ()()
Example 2:
Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""
from collections import deque


def generate_valid_parentheses(num):
    ans = deque([""])
    cnt = deque([(0, 0)])
    for i in range(2 * num):
        for j in range(len(ans)):
            par = ans.popleft()
            l_cnt, r_cnt = cnt.popleft()
            if l_cnt < num:
                ans.append(par + r"(")
                cnt.append((l_cnt + 1, r_cnt))
            if r_cnt < l_cnt:
                ans.append(par + r")")
                cnt.append((l_cnt, r_cnt + 1))
                # r_cnt <= l_cnt
    return ans


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()


"""
The n-th Catalan number is bounded by O(2^{2n}/(n*sqrt{n}))
Time/Space: O(2^{2n}/sqrt{n}) 
"""
