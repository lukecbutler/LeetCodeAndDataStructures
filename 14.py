'''
Result: failed - 1.5 hours spent

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
    index = 0

    # base case for list with single item
    if len(strs) == 1:
        return strs[0]

    # empty list basecase:
    while True:
        for word in strs: # loop thru list

            # base case for empty string
            if len(word) == 0: 
                return ''
            

            # main logic
            try:
                if word[index] == longestPrefix[index]:
                    continue
            except:
                # base case to add first character of word
                if len(longestPrefix) == 0: # base case to add first character of s
                    longestPrefix.append(word[index])

                longestPrefix = longestPrefix[:-1]

                string = ''.join(longestPrefix)

                return string

            else:
                longestPrefix = longestPrefix[:-1]

                string = ''.join(longestPrefix)

                return string # change this to the longest prefix minus last character

        index += 1

        try:
            longestPrefix.append(word[index])
        except:
            longestPrefix = longestPrefix[:-1]

            string = ''.join(longestPrefix)

            return string # change this to the longest prefix minus last character


    


strs = ["ab", "a"]
output = longestCommonPrefix(strs)

print(f"Text Case:{output}")