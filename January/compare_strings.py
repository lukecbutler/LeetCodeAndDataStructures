def compare_strings(s1: str, s2: str) -> int:

    s1split = list(s1)
    s2split = list(s2)

    i = 0
    while i < len(s1) and i < len(s2):
        if s1split[i] < s2split[i]:
            return -1

        if s1split[i] > s2split[i]:
            return 1

        i += 1
        
    return 0


s1 = "hello"
s2 = "hello"

print(compare_strings(s1, s2))