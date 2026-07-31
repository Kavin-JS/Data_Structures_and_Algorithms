def maxProfit(prices):
    minPrice = float("inf")
    profit = 0
    for p in prices:
        if p < minPrice:
            minPrice = p
        else:
            profit = max(profit, p - minPrice)
    return profit

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
