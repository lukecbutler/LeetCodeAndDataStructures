'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs: list[str]) -> str:

    longestPrefix = []
    for string in strs:
        for letter in string:
            # add the first word to the common prefix
            longestPrefix.append(letter)
            break


    for i in longestPrefix:
        if i == i :
            return True


    return longestPrefix


strs = ["flower","flow","flight"]
output = longestCommonPrefix(strs)

print(f"Text Case:{output}")