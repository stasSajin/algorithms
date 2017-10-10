# Uses python3
import sys
def get_fibonacci_last_digit_naive(n):
    # set the base case
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        previous, current = current, previous + current % 10

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #n = int(input())
    print(get_fibonacci_last_digit_naive(n))
