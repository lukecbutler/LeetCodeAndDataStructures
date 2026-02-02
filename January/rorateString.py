"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    left = 0
    right = len(s)-1

    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp

        left += 1
        right -= 1
    
    return s
        


s = ["l","u","k","e"]
print(reverseString(s))
