

nums = [3,1,2,10,1]

def runningSum(nums):
    newList = []
    for i in range(len(nums)):
        if i == 0:
            newList.append(nums[i])
        else:
            newList.append(newList[i-1] + nums[i])
    print(newList)
    return newList

runningSum(nums=nums)


def prac(nums):
    newList = []
    for i in range(len(nums)):
        print(i)

prac(nums)