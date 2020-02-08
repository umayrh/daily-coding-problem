"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
from math import pow, pi
from random import uniform


def make_pi(precision: int):
    """
    Monte Carlo sampling inside a square of length 2 centered at origin, and an inscribed
    circle of radius 1 centered at origin. Ratio of the area of the circle and square = pi/4.
    Rule of thumb: each significant digit costs 100 samples
    :param precision: Number of decimal places in the pi estimate
    :return: value of pi to given precision
    """
    num_samples = round(pow(10, (precision + 1) * 2))
    count = 0
    for idx in range(num_samples):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x*x + y*y <= 1:
            count = count + 1
    estim = (4.0 * count) / num_samples
    print(estim, count, round(estim, precision), round(pi, 3))
    return round(estim, precision)


if __name__ == "__main__":
    assert make_pi(3) == round(pi, 3)
