
def numberOfSteps(num):
    numStepsCounter = 0
    while num != 0:
        if num % 2 == 0:
            numStepsCounter += 1
            num = num / 2
            continue
        else:
            numStepsCounter += 1
            num = num - 1
            continue
    print(numStepsCounter)
    return numStepsCounter

numberOfSteps(8)