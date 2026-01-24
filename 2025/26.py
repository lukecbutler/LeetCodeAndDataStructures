'''
result: 53 minutes ; no outside help

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k.
After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, 
with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

def removeDuplicates(nums: list[int]) -> int:
    print(f"Original nums array: {nums}")

    seenIntegers = []
    k = 0
    indexCounter = 0

    # set all reoccurances of numbers to 'x'
    for number in nums:
        if number in seenIntegers: #check if present
            nums[indexCounter] = 'x' # set num[index] to 'x'

            indexCounter += 1 #increment index
        else:
            seenIntegers.append(number)
            k+=1
            indexCounter += 1

    for element in range(len(nums)):
        if 'x' in nums:
            nums.remove('x') # remove first occurance of 'x'
            nums.append('x') # append 'x' to the end
        else:
            continue

    
    # seen integers needs to be nums
    print(f'Modified nums array:  {nums}')

    # k
    print(f'k: {k}')
    return k




nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums=nums)