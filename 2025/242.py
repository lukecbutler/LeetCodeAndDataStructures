'''
Result: 27m - no outside help

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

def isAnagram(s: str, t: str) -> bool:
    sMap = {}
    tMap = {}

    #if t & s are not same length, return false
    if len(s) != len(t):
        return False

    for i in s: # Create s frequency map
        if i not in sMap:
            sMap[i] = 1
        else:
            sMap[i] += 1

    for i in t: # Create t frequency map
        if i not in tMap:
            tMap[i] = 1
        else:
            tMap[i] += 1

    for i in t: 

        # Check if all characters are present
        if i not in sMap:
            return False 
        
        # Check if values of characters match in the two frequency maps
        elif tMap.get(i) != sMap.get(i):
            return False
        

    return True



print("TEST CASE:")
s = "rat"
t = "car"

print(isAnagram(s=s, t=t))