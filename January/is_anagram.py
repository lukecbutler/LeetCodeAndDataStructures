def is_anagram(s: str, t: str) -> bool:

    # build frequency map of string 's'
    s_map = {}
    for char in s:
        if char in s_map:
            s_map[char] += 1
        else:
            s_map[char] = 1

    # build frequency map of string 't'
    t_map = {}
    for char in t:
        if char in t_map:
            t_map[char] += 1
        else:
            t_map[char] = 1

    if s_map == t_map:
        return True
    else:
        return False
        

    

if __name__ == "__main__":
    s = "listen"
    t = "silent"
    print(is_anagram(s, t))
