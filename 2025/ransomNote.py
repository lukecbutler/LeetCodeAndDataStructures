'''
Result: 46 minutes

Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
'''


def canConstruct(ransomNote: str, magazine: str) -> bool:
    frequencyMap = {}

    # Create a frequency map out of the characters in magazine
    for magazineCharacter in magazine: 
        if magazineCharacter in frequencyMap:
            frequencyMap[magazineCharacter] += 1
        else:
            frequencyMap[magazineCharacter] = 1
    
    # Check if characters in ransomNote can create magazine

    # Loop through ransomNote & check if letter of i is contained in the frequency map
    for ransomNoteCharacter in ransomNote:
        print(ransomNoteCharacter)
        if ransomNoteCharacter in frequencyMap:
            #decrement value in key-value pair of frequencyMap
            frequencyMap[ransomNoteCharacter] -= 1

            # check if value of character has hit -1
            if frequencyMap[ransomNoteCharacter] < 0:
                return False
            continue
        else:
            return False
    # If any letter is NOT contained, return false

    return True

ransomNote = "abbb"
magazine = "abb"
print(canConstruct(ransomNote, magazine))