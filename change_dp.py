def find_ways(amount, denoms):
    if amount in memo:
        return memo[amount]
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    
    sub_ways = 0
    for denom in denoms:
        sub_ways += find_ways(amount-denom, denoms)
    memo[amount] = sub_ways
    return sub_ways

if "__main__" == __name__:
    total = 110 # total amount we are given from which we must find change, you can change this
    denominations = [1, 5]

    memo = {1:1}
    ways = find_ways(total, denominations)
    print(ways)
    
    # you could actually solve this problem bottom up
    # find the number of ways to get a certain amount
    # then just build upwards
    memo = {}
    for i in range(1, total+1):
        sub_ways = 0
        for denom in denominations:
            if i-denom < 0:
                continue
            if i - denom in memo:
                sub_ways += memo[i-denom]
            elif i - denom == 0:
                sub_ways += 1
                memo[i-denom] = 1
        memo[i] = sub_ways
    print(memo[total])
    # notice that the time complexity becomes obvious => O(T*D)
    # where T is the total amount and D is the number of denominations we have