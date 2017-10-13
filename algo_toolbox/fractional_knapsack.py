# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # find the ratio between weights and values
    # get the values of reward ratios by dividing the value/weights
    current_weight = 0
    reward = []
    for values, weight in zip(values, weights):
        reward.append(values/weight)
    # sort the reward ratios
    data=sorted(zip(reward,weights), reverse = True)
    reward, weights = [list(tup) for tup in zip(*data)]
    # calculate the weight
    i = 0 # starting index
    while current_weight < capacity and i < len(weights):
        if weights[i] <= capacity - current_weight:
            value += (reward[i] * weights[i])
            current_weight += weights[i]
            i +=1
        else:
            value += reward[i] * (capacity - current_weight)
            current_weight += weights[i]
            i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
