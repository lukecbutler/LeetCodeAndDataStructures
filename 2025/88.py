'''
Result: 43 minutes - no outside help(videos/articles/ai)!!!


You are given two integer arrays nums1 and nums2, sorted in increasing order
m = length of list nums1
n = length of list nums2

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.


Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]

Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].
'''

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    print(f"nums1 array: {nums1}\n")
    print(f"numbers in num1 array: {m}\n")
    print(f"nums2 array: {nums2}\n")
    print(f"numbers in num2 array: {n}\n")


    for array2Number in range(n):
        nums1[m] = nums2[array2Number]
        m += 1
        if m > len(nums1):
            break

    # sort list nums 1 in increasing order
    nums1.sort()


    return nums1


nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))