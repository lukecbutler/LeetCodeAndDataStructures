'''
The Challenge: Given a list nums and a target, find two numbers that add up to the target and return their indices.

nums = [2, 7, 11], target = 9
Result: [0, 1] (because nums[0] + nums[1] = 9)

The Tool: Instead of seen = set(), we use prev_map = {}.

Key: The number.

Value: The index where we found it.
'''

def twoSums(nums, target):
    frequency_map = {}

    for i in range(len(nums)): # make frequency map
        frequency_map[nums[i]] = i

    for i in frequency_map:
        for j in frequency_map:
            if i + j == target:
                firstValue = frequency_map[i]
                secondValue = frequency_map[j]
                return [firstValue, secondValue]

    return False # return false if no indices add up to target

nums = [2, 7, 11]
target = 9

print(twoSums(nums=nums, target=target))
