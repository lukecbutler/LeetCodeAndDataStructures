'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
import math

#logic: 
# 1. if number is negative, flip to positive -> 
# 2. square the number -> 
# 3. append the squared number to the array -> 
# 4. sort the array
# 5. return the array

def sortedSquares(nums: list[int]) -> list[int]:
    squared = []

    for number in nums:
        if number < 0:
            number = abs(number)
        
        number = number * number
        squared.append(number)

    squared.sort()
    
    return squared


if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums=nums))