# Uses python3
import sys

def get_change(t):
    #write your code here
    c = 0
    if t >= 10:
        tens = t//10
        c += tens
        t = t - 10*tens
    if t >= 5:
        fives = t//5
        c = fives + c
        t = t - 5*fives
    return c + t

if __name__ == '__main__':
    t = int(sys.stdin.read())
    print(get_change(t))
