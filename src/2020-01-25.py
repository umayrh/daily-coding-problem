"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from typing import List, Set
Vector = List[int]
IntSet = Set[int]


def one_pass_pair_sum(user_list: Vector, k: int):
    if not user_list:
        return False
    int_set: IntSet = set()
    for item in user_list:
        rem = k - item
        int_set.add(item)
        if rem in int_set:
            return True
    return False


if __name__ == "__main__":
    input_list = [10, 15, 3, 7]
    k = 17
    result = one_pass_pair_sum(input_list, k)
    print(f"{k} in {input_list}: {result}")

    k = 19
    result = one_pass_pair_sum(input_list, k)
    print(f"{k} in {input_list}: {result}")
