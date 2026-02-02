'''Given a string s, return true if it is a palindrome, or false otherwise.'''




def isPalindrome(s: str) -> bool:
    if len(s) == 1 or len(s) == 0: # Base-case
        return True
    
    string_to_check = []

    # apply .lower() to string
    s = s.lower()

    #core logic:
    for i in s:
        if i.isalpha() or i.isnumeric(): #isalpha() checks if i is a letter; isnumeric() checks if i is a number. AlphaNumeric characters are letters or numbers.
            string_to_check.append(i)

    "".join(string_to_check)

    if string_to_check == string_to_check[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    s = "P0"
    print(isPalindrome(s))
