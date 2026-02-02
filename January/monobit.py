def countMonobit(n: int) -> int:
    # core logic
    monobitCount = 0

    if n == 0:
        return 1

    for i in range(1, n+1):
        binary = []
        flag = True
        number = n

        while flag:

            if number == 0:
                binary.append(0)
                break

            if number // 2 == 0:
                binary.append(1)
                flag = False
            
            else:
                binary.append(number % 2)
                number = number // 2

        binary = binary[::-1]

        # this is some wild logic right here
        monobitCount += 1
        for i in binary:
            if i == 0:
                monobitCount -= 1
                break
    


    return monobitCount

if __name__ == "__main__":
    n = 3
    print(countMonobit(n))