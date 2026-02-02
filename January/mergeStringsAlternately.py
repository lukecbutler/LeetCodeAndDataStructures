#O(n)

def mergeAlternately(word1: str, word2: str) -> str:
    result = [] # Box to hold final string
    i, j = 0, 0 # Set i & j to 0

    # Merge while both strings have characters
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    # Append the remainder of whichever string is longer
    result.append(word1[i:])
    result.append(word2[j:])

    return "".join(result)


word1 = "hello"
word2 = "world"
print("TEST CASE")
print(mergeAlternately(word1, word2))