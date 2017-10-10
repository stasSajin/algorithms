# Uses python3
f = dict()
def calc_fib(n):
    """
    This function implements fibonacci function using memoization.
    """
    if (n <= 1):
        return n
    try:
        return f[n]
    except:
        f[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return f[n]

n = int(input())
print(calc_fib(n))
