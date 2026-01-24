"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1, 2, 3, 1]
Output: true (because 1 appears twice)

Input: nums = [1, 2, 3, 4]
Output: false (all unique)
"""

def containsDuplicate(nums):
    # Initialize an empty set - set it used as they have constant time checking and fundamentally only contain one unique element, perfect for this use case
    seen = set()
    

    for num in nums:
        if num in seen:
            return True
        if num not in seen: # is there a difference here between 'num not in seen' and just an else?
            seen.add(num)
        
    return False # Return false if number never seen inside of the set



nums = [1, 2, 3, 4]

print("TEST CASE:")
print(containsDuplicate(nums=nums))
print("Expected: FALSE")