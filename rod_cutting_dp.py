#Kent Tran

import time

def rod_cutting_dp(price, n):
    dp = [0] * (n + 1)

    for i in range (1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], price[j - 1] + dp[i - j])

    return dp[n]

def driver_dp(price):
    n = len(price)

    start_time = time.time()
    max_profit = rod_cutting_dp(price, n)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Size of array: {n}")
    print(f"Max profit: {max_profit}")
    print(f"Code execution time: {execution_time} seconds")