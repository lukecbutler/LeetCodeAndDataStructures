'''
Result: 13 minutes - PR! ; Side note: Figure out process for solving these questions, staring at the question & writing down thoughts is to hit & miss

Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

def strStr(haystack: str, needle: str) -> int:

    # needle need to stay string
    for i in range(len(haystack)):
        if haystack[i:len(needle)+i] == needle:
            return i
        else:
            continue
 

    # return -1 if needle is not in haystack
    return -1


print("TEST CASE 1:")
haystack = "sabutad"
needle = "sad"
print(strStr(haystack=haystack, needle=needle))