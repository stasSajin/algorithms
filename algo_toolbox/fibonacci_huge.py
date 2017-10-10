# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n


    previous = 1
    current  = 1
    cycle_len = 1 # starting at 1 since out `previous` starts at 1 rather than 0
    # set up the initial sequence of numbers
    f_modulo = [0, 1, 1]
    for _ in range(2, n):
        cycle_len += 1
        previous, current = current, (previous + current) % m
        f_modulo.append(current)
        if previous == 0 and current == 1:
            cycle_len = cycle_len
            new_n = n % cycle_len
            return f_modulo[new_n]
    # if the n of fibonacy_modulo is smaller than the cycle, return f[n]
    return f_modulo[n]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
