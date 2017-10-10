# Uses python3
import sys


def gcd_naive(a, b):
    # this is version 1 implementation
    current_gcd = 1
    smallest = a if a < b else b
    largest = a if a > b else b
    i = 2
    # let's find the factors for the smallest number
    while i < smallest + 1:
        if smallest % i == 0 and largest % i == 0:
            current_gcd = current_gcd * i
            smallest = smallest//i
            largest = largest//i
        else:
            i += 1
    return current_gcd

def gcd_naive2(a, b):
    # this is version 2 implementation that checks the factors for smallest
    current_gcd = 1
    smallest = a if a < b else b
    largest = a if a > b else b
    i = 2
    # let's find the factors for the smallest number
    factors_smallest = []
    while i < smallest + 1:
        if smallest % i == 0:
            factors_smallest.append(i)
            smallest = smallest//i
        else:
            i += 1
    print(factors_smallest)
    for factor in factors_smallest:
        if largest % factor == 0:
            current_gcd = current_gcd * factor
            largest = largest // factor

    return current_gcd

def EuclidGCD(a, b):
    # this is version 3 implementation using Euclidian method
    if b == 0:
        return a
    a = a % b
    return(EuclidGCD(b, a))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(EuclidGCD(a, b))
