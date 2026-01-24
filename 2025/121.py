'''
Result; conflicted - passed most test cases, but used gemini to help solve the last couple.

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
------------------------------------------------------------------------------------------------------------------------------------------------------
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

def maxProfit(prices: list[int]) -> int:
    low = prices[0] # init low to first int in array
    high = prices[0] # init high to first int in array
    bestReturn = -1 # needs to be set to high - low (at some point)

    # loop thru list once
    for i in prices:
        if i > high:
            high = i
            bestReturn = high - low
        elif i < low:
            low = i
            high = i
        else:
            continue

    return bestReturn

prices = [3,2,6,5,0,3]
print(maxProfit(prices=prices))

'''
    if high == low:
        return 0
    else:
        return bestReturn
'''