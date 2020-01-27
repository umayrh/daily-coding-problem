"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from math import log, exp
from typing import List
Vector = List[int]


def set_minus_one_product(user_list: Vector):
    if not user_list:
        return 0
    product = 1
    for item in user_list:
        product *= item
    result: Vector = list()
    for item in user_list:
        result.append(int(product / item))
    return result


def set_minus_one_product_no_div(user_list: Vector):
    if not user_list:
        return 0
    product = 1
    for item in user_list:
        product *= item
    log_product = log(product)
    result: Vector = list()
    for item in user_list:
        result.append(round(exp(log_product - log(item))))
    return result


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    result = set_minus_one_product(input_list)
    print(f"for {input_list}: {result}")

    result = set_minus_one_product_no_div(input_list)
    print(f"for {input_list}: {result}")
