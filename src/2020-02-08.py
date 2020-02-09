"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
from random import randint


def uniform_sample(sample: int, reservoir: list, reservoir_size: int, count: int):
    if len(reservoir) < reservoir_size:
        reservoir.append(sample)
        return count + 1
    sample_prob = randint(1, count + 1)
    if sample_prob == count + 1:
        replace_prob = randint(0, reservoir_size - 1)
        reservoir[replace_prob] = sample
    return count + 1


if __name__ == "__main__":
    count = 0
    reservoir = list()
    for num in range(100):
        count = uniform_sample(num, reservoir, 1, count)
        print(reservoir)
