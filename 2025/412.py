n = 15


newList = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        newList.append("FizzBuzz")
        continue
    if i % 3 == 0:
        newList.append("Fizz")
        continue
    if i % 5 == 0:
        newList.append("Buzz")
        continue
    else:
        newList.append(str(i))

print(newList)