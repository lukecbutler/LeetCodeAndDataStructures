'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

O(N) solution - linear time

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# check for two indices adding to the target value, while builing the seen map
# hashmap construction: key = index ; value = element ; ex. {2:0}, where 2 is the element & 0 is the index
# 
def twoSum(nums, target):

    index_map = {}

    for i in range(len(nums)):
        current_num = nums[i]
        complement = target - current_num

        if complement in index_map:
            return [index_map[complement], i]
        
        index_map[current_num] = i


nums = [2, 7, 11]
target = 9
print(twoSum(nums=nums, target=target))
