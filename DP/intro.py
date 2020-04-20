def fib(x):
    if x == 1 or x == 2:
        return x
    return fib(x-1) + fib(x-2)

def fib_DP(x):
    dp = [1 for _ in range(x)]
    for i in range(2, x):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[x-1]

x = 5
res = fib_DP(x)

print(res)