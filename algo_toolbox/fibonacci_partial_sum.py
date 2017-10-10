# Uses python3
import sys

def fibonacci_partial_sum(a, b):
    previous = 1
    current  = 1
    cycle_len = 1 # starting at 1 since out `previous` starts at 1 rather than 0
    # set up the initial sequence of numbers
    f_modulo = [0, 1, 1]
    for _ in range(2, a):
        cycle_len += 1
        previous, current = current, (previous + current) % 10
        f_modulo.append(current)
        if previous == 0 and current == 1:
            f_modulo.pop()
            f_modulo.pop()
            rem = n % cycle_len
            return b + rem/cycle_len - 1

    # if the n of fibonacy_modulo is smaller than the cycle, return f[n]
    return sum(f_modulo)%10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(a, b))
