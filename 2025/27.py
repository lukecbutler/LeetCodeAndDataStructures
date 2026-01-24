'''
Result: 43 minutes ; no outside help

Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.

Return k.

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''


def removeElement(nums: list[int], val: int) -> int:
    k = 0
    currentIndex = 0
    for number in nums:
        if number == val:
            nums[currentIndex] = 'x'
        else:    
            k += 1
        currentIndex += 1
    #bug here
    for i in range(len(nums)):
        try:
            nums.remove('x')
        except:
            continue

    print(nums)
    return k
'''
print("TEST CASE 1:")
nums = [3,2,2,3]
val = 3
print(removeElement(nums=nums, val=val))
'''

print("------------------")

print("TEST CASE 2:")
nums2 = [2,2,3]
val2 = 2
print(removeElement(nums=nums2, val=val2))