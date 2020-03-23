def fastFib(n, memo):
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

def fibonacci(n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)

fibonacci(100)
print(memo)