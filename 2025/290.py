'''
Result: 55 minutes. Had to look up muliple logic questions, specifically around dictionaries & how to check for values & keys in dictionaries

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".
'''

# no two letters can map to the same word - check for this
def wordPattern(pattern: str, s: str) -> bool:
    patternMapping = {}
    s = s.split()

    if len(s) != len(pattern): # length of words & pattern is not equal edge case
        return False
    
    for letter in range(len(pattern)): # loop through amount ofletters in pattern

        if pattern[letter] not in patternMapping: # add mapping from pattern to s
            patternMapping[pattern[letter]] = s[letter]


            # check if word is mapping to 2 different letters
            values = patternMapping.values()
            if len(values) != len(set(values)):
                return False
            

        elif s[letter] != patternMapping[pattern[letter]]:
            return False

    return True
            #if not correct, return false


print("TEST CASE:")
pattern = "aaa"
s = "aa aa aa aa"

print(wordPattern(pattern=pattern, s=s))