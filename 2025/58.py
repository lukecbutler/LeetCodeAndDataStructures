'''
Result = 19m

Given a string s consisting of words and spaces, return the length of the last word in the string.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
'''

def lengthOfLastWord(s: str) -> int:
    
    # how do I account for space before & after??
    inLastWord = False
    newString = []

    if len(s) == 0: #empty string case
        return 0
    
    # space before last word case
    for e in reversed(s):
        if e == ' ' and inLastWord == False: #skip all spaces
            continue

        elif e != ' ': # add letters of word
            newString.append(e)
            inLastWord = True

        elif e == ' ' and inLastWord == True:
            break   

    return len(newString)


test1 = "Hello    World      "
output = lengthOfLastWord(test1)

# --- Test Case 1 ---
print(f"Test 1:{output}")