# Uses python3
import sys

def lcm(a, b):
    smallest = a if a < b else b
    largest = a if a > b else b
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
