"""
LC 93
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def is_num_valid(s):
            return s and str(int(s)) == s and int(s) <= 255
            
        def is_split_valid(p1, p2, p3):
            return all(map(is_num_valid, (s[l: r] for l, r in pairwise((0, p1, p2, p3, len(s))))))
        
        for p1 in range(1, 4):
            for p2 in range(p1 + 1, p1 + 4):
                for p3 in range(p2 + 1, p2 + 4):
                    if is_split_valid(p1, p2, p3):
                        res.append(".".join(s[l: r] for l, r in pairwise((0, p1, p2, p3, len(s)))))  
                        
        return res
                    
                    
"""
Time/Space O(1)
"""
