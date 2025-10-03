
# Given an integer n, 
# return a string array answer

'''
Given an integer n, return an array of strings where:
- "FizzBuzz" if i is divisible by 3 and 5;
- "Fizz" if i is divisible by 3;
- "Buzz" if i is divisible by 5;
- i as a string is not divisible by 3 or 5;
'''
def fizzBuzz(n):
    newArray = []
    for i in range(1, n+1):

        if i % 3 == 0 and i % 5 == 0:
            newArray.append("FizzBuzz")

        elif i % 3 == 0:
            newArray.append("Fizz")

        elif i % 5 == 0:
            newArray.append("Buzz")

        else: 
            newArray.append(str(i))

    return newArray



print(fizzBuzz(15))