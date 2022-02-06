"""
LC 6003
You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does not contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.

As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:

Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.
Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.
Remove a train car from anywhere in the sequence which takes 2 units of time.
Return the minimum time to remove all the cars containing illegal goods.

Note that an empty sequence of cars is considered to have no cars containing illegal goods.

 

Example 1:

Input: s = "1100101"
Output: 5
Explanation: 
One way to remove all the cars containing illegal goods from the sequence is to
- remove a car from the left end 2 times. Time taken is 2 * 1 = 2.
- remove a car from the right end. Time taken is 1.
- remove the car containing illegal goods found in the middle. Time taken is 2.
This obtains a total time of 2 + 1 + 2 = 5. 

An alternative way is to
- remove a car from the left end 2 times. Time taken is 2 * 1 = 2.
- remove a car from the right end 3 times. Time taken is 3 * 1 = 3.
This also obtains a total time of 2 + 3 = 5.

5 is the minimum time taken to remove all the cars containing illegal goods. 
There are no other ways to remove them with less time.
Example 2:

Input: s = "0010"
Output: 2
Explanation:
One way to remove all the cars containing illegal goods from the sequence is to
- remove a car from the left end 3 times. Time taken is 3 * 1 = 3.
This obtains a total time of 3.

Another way to remove all the cars containing illegal goods from the sequence is to
- remove the car containing illegal goods found in the middle. Time taken is 2.
This obtains a total time of 2.

Another way to remove all the cars containing illegal goods from the sequence is to 
- remove a car from the right end 2 times. Time taken is 2 * 1 = 2. 
This obtains a total time of 2.

2 is the minimum time taken to remove all the cars containing illegal goods. 
There are no other ways to remove them with less time.
"""
class Solution:
    def minimumTime(self, s: str) -> int:
    	# 0 l1 l2 l3 l4
    	#  \  \  \  \  \
     	#   r4 r3 r2 r1 0
        left = [0]
        best = 0
        for i, c in enumerate(s):
            if c == '0':
                continue
            # one-by-one, or just remove
            best = min(i + 1, best + 2)
            left.append(best)
            
        right = []
        best = 0
        for i, c in enumerate(reversed(s)):
            if c == '0':
                continue
            # one-by-one, or just remove
            best = min(i + 1, best + 2)
            right.append(best)
        right.reverse()
        right.append(0)
            
        return min(map(sum, zip(left, right)))


"""
Time/Space O(N)
"""
