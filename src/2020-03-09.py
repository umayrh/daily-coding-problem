"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform
probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
from random import randint


def rand5() -> int:
    return randint(1, 5)


def rand7() -> int:
    table = []
    for idx in range(0, 7):
        table[idx] = idx * 5 + rand5()
    


if __name__ == "__main__":
    histogram = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for _ in range(777):
        histogram[rand7()] += 1
    print(histogram)
