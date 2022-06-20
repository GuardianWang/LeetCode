"""
LC 202
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
"""


def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
        if slow == fast:
            return slow == 1


def next_num(n):
    new = 0
    while n != 0:
        new += (n % 10) ** 2
        n = n // 10

    return new


def main():
    print(find_happy_number(23))  # T
    print(find_happy_number(12))  # F


main()


"""
Time O(logN): next_num(N) is logN, and thus it takes logN time to reach < 1000, 
then it takes < 1001 O(1) iterations.
logn + loglogn + ... is logn
Space O(1)
"""
