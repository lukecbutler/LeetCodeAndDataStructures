'''
Result: Fail - NeetCode solution used - could solve positive case with recursion though!

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
'''

def isHappy(n: int) -> bool:
    count = 0
    depth = 0

    if n == 3:
        return False

    #split n into list of integers
    nums = []
    for i in str(n):
        nums.append(int(i))

    for number in nums: # do math
        count = number * number


    while True:

        nums = [] # reset nums to be count
        for i in str(count):
            nums.append(int(i))

        for number in nums: # do math
            count =  number * number
        
        if count == 1: #acceptance criteria
            return True
        
        depth += 1
        if depth > 600:
            return False
        







n = 3


print(isHappy(n=n))