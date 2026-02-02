"""
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"
"""

def gcdOfStrings(str1: str, str2: str) -> str:
    gcd = [] # final gcd
    finalGCD = [] # temporary gcd

    i = 0
    while i < len(str1) and i < len(str2): # run for the shortest string
        if str1[i] == str2[i]:
            gcd.append(str1[i])
        i += 1
            



    return gcd




str1 = "ABCABC"
str2 = "B"

print(gcdOfStrings(str1, str2))