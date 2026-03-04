def integerToBinary(integer) -> list:
    binaryArray = []
    while integer > 0:
        binaryArray.append(integer % 2)
        integer = integer // 2
    binaryArray.reverse()
    return binaryArray

def areMonobit(binaryArray) -> bool:
# input: list of binary integers
# output: true if all one's
    set(binaryArray)
    if 0 in binaryArray:
        return False
    else:
        return True
    
def countMonobit(n: int) -> int:
# input: integer
# output: number of integers in the range of [0, n] that are monobit
    count = 0
    for i in range (n+1):
        integerInBinary = integerToBinary(i) # convert integer to binary array
        mobitOrNot = areMonobit(integerInBinary) # return true if it is monobit
        if mobitOrNot == True: # add to counter if the integer is monobit
            count += 1
        else:
            continue

    return count


if __name__ == "__main__":
    integer = 4
    binaryRepresentation = integerToBinary(integer=integer) #1
    ifMonoBit = areMonobit(binaryRepresentation) #2
    print(countMonobit(4))
