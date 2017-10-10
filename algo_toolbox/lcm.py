# Uses python3
import sys

def EuclidGCD(a, b):
    # this is version 3 implementation using Euclidian method
    if b == 0:
        return a
    a = a % b
    return(EuclidGCD(b, a))

def lcm(a, b):
    # and the lcf = a*b/gcf
    gcf = EuclidGCD(a, b)
    return a*b//gcf

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
