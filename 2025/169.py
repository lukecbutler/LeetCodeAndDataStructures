'''
Result: 20 minutes ; Looked up frequency maps in notes, 
then looked at article on how to return the highest value of a dictionary, and it's associated key.

Takeaway: Dictionaries/ hashmaps are a weakpoint.
----------------------------------------------------------------------------------------------------
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 
Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

def majorityElement(nums: list[int]) -> int:
    majorityElement = None

    # create frequency map of all numbers
    frequencyMap = {}
    for number in nums:
        if number in frequencyMap:
            frequencyMap[number] += 1
        else:
            frequencyMap[number] = 1

    # return the key with the highest value

    majorityElement = max(frequencyMap, key=frequencyMap.get)

    return majorityElement

print(majorityElement([3,2,3]))


