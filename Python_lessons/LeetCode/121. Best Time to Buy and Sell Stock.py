def maxProfit(prices) -> int:
    bestbuy = prices[0]
    bestsell = prices[0]
    mprofit = 0
    for el in prices:
        profit = el - bestbuy
        if profit > mprofit:
            mprofit = profit
        if el < bestbuy:
            bestbuy = el
        if el > bestsell:
            bestsell = el
    return mprofit

a = [7,12,1,5,3,6,11,4]
print(maxProfit(a))
