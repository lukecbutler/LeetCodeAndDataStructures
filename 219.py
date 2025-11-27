'''
Result: Solved ~1 hour

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    latestSeen = {}
    for number in range(len(nums)):

        if nums[number] in latestSeen: # check if integer is already present
            # check if new index - old index >= k
            if  k >= number - latestSeen[nums[number]]:
                return True

        latestSeen[nums[number]] = number # add all last occurance of integer to value of key

    return False


print("TEST CASE 1:")
nums = [1,0,1,1]
k = 1


print(containsNearbyDuplicate(nums=nums, k=k))