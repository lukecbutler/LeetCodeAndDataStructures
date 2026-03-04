def removeDuplicates(nums: list[int]) -> int:
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

        right += 1

    # pop (right - 1) - left number of times
    for i in range(right- 1 - left):
        nums.pop()
        
    return nums


if __name__ == '__main__':
    nums = [1,1,2]
    print(removeDuplicates(nums=nums))

