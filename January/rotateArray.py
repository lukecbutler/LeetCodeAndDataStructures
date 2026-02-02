def rotate_array(nums: list[int], k: int) -> list[int]:
    new_array = []

    if k == 0:
        return nums

    normal_k = k % len(nums) # avoid unecessary rotations

    #split array into front and back halves
    front_half = nums[0:normal_k+1]
    back_half = nums[normal_k+1:]

    new_array = back_half + front_half

    return new_array

nums = [1, 2, 3, 4, 5]
k = 2

print(rotate_array(nums, k))

