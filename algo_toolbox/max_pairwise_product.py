# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


largest = 0
second_largest = 0

for i in a:
    if i >= largest:
        second_largest, largest =  largest, i
    if i > second_largest and i < largest:
        second_largest = i

print(largest * second_largest)
