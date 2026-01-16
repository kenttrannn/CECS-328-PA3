#Kent Tran

import time

def rod_cutting_recursive(price, index, n):
    if n == 0 or index < 0:
        return 0
    
    if index + 1 > n:
        return rod_cutting_recursive(price, index - 1, n)
    
    cut = price[index] + rod_cutting_recursive(price, index, n - (index + 1))
    not_cut = rod_cutting_recursive(price, index - 1, n)

    return max(cut, not_cut)

def driver_recursive(price):
    n = len(price)

    start_time = time.time()
    max_profit = rod_cutting_recursive(price, n - 1, n)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Size of array: {n}")
    print(f"Max profit: {max_profit}")
    print(f"Code execution time: {execution_time} seconds")