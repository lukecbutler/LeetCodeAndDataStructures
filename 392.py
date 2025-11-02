'''
Result: 40 minutes - had to look up how to remove first element from a string

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

def isSubsequence(s: str, t: str) -> bool:

    if s == "": # empty string edge case
        return True
    
    if s == t: # s & t are same edge case
        return True
    
    if len(s) == len(t): # s & t are same length edge case expanded
        if s == t:
            return True
        else:
            return False

    for tLetter in range(len(t)):
        if s[0] == t[tLetter]:
            if len(s) == 1:
                return True
            
            s = s[1:]

            if len(s) == 0:
                return True
        continue

    return False


print("TEST CASE 1:")
s = "bb"
t = "ahbgdc"

print(isSubsequence(s=s, t=t))

