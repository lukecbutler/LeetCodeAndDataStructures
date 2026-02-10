'''
The Challenge: Given a list nums and a target, find two numbers that add up to the target and return their indices.

nums = [2, 7, 11], target = 9
Result: [0, 1] (because nums[0] + nums[1] = 9)

The Tool: Instead of seen = set(), we use prev_map = {}.

Key: The number.

Value: The index where we found it.
'''

def twoSums(nums, target):
    index_map = {}

    for i in range(len(nums)):
        current_num = nums[i]
        complement = target-current_num
        print(complement)

        if complement in index_map:
            return [index_map[complement], i]
        else:
            index_map[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSums(nums=nums, target=target))
