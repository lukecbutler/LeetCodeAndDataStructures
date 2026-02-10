'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

O(N) solution - linear time

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# check for two indices adding to the target value, while builing the seen map
# hashmap construction: key = element ; value = index ; ex. {2:0}, where 2 is the element & 0 is the index

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target and i!=j:
                return [i,j]




nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums=nums, target=target))
