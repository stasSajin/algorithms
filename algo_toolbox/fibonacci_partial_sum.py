# Uses python3
import sys

def fibonacci_partial_sum(a, b):
    previous = 1
    current  = 1
    cycle_len = 1 # starting at 1 since out `previous` starts at 1 rather than 0
    # set up the initial sequence of numbers
    f_modulo = [0, 1, 1]
    for _ in range(2, b):
        cycle_len += 1
        previous, current = current, (previous + current) % 10
        f_modulo.append(current)
        if previous == 0 and current == 1:
            f_modulo = f_modulo[:-2]
            rem_a = a % cycle_len
            rem_b = b % cycle_len

            # generate sum of digits from f to end of nearest cycle
            sum_a = sum(f_modulo[rem_a:])
            # generate sum of digits from start of nearest cycles to f2
            sum_b = sum(f_modulo[:rem_b+1])
            # generate sum digits for complete cycles between f1 and f2
            return (sum_a + sum_b) % 10

    # if the n of fibonacy_modulo is smaller than the cycle, return f[n]
    return sum(f_modulo[a:b+1]) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    a, b = map(int, input.split())
    print(fibonacci_partial_sum(a, b))
