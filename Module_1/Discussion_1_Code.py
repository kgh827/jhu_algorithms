import time

# Naive recursive Fibonacci
def fib_naive(n: int, counter: list) -> int:
    counter[0] += 1
    if n <= 1:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)

# Dynamic programming Fibonacci
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    F = [0] * (n + 1)
    F[0], F[1] = 0, 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

n = 40

# Naive recursion measurement
counter = [0]
t0 = time.perf_counter()
val_naive = fib_naive(n, counter)
t1 = time.perf_counter()

# Dynamic programming measurement
t2 = time.perf_counter()
val_dp = fib_dp(n)
t3 = time.perf_counter()

print(f"n={n}")
print(f"Naive recursion: fib={val_naive:,} | calls={counter[0]:,} | time={t1 - t0:.4f}s | space=O(n) call stack depth")
print(f"DP (table):      fib={val_dp:,} | time={t3 - t2:.6f}s | space=O(n) array/list storage")
