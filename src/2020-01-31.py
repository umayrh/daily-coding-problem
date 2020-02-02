"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
from typing import Dict
CodeMap = Dict[str, int]
RevMap = Dict[str, str]
SetMap = Dict[str, set]


def count(code_map: CodeMap, code_str: str, use_cache: bool = True):
    """
    This solution should work for codes maps with arbitrary number of digits.

    Examples:
      111111=aaaaaa,kaaaa,akaaa,aakaa,aaaka,aaaak,kkaa,kaka,kaak,akka,aakk,akak,kkk (6x5/2 - 2 = 13)
      22222=,bbbbb,vbbb,bvbb,bbvb,bbbv,vvb,vbv,bvv (5x4/2 - 2 = 8)
      22227=bbbbg,vbbg,bvbg,bbvg,vvg (4x3/2 - 2 = 4 != 5...?)
      1111=aaaa,kaa,aka,aak,kk
      abcd = ab.cd, ac.bd, ad.bc, bc.ad, bd.ca, cd.ad
      111=aaa,ak,ka (3x2/2 - 2 = 1 != 3...?)
    Assuming for now the mapping contains a consistent set of ints e.g. if there's a mapping for 21,
      then there's also a mapping for 1 and 2. This probably can be easily relaxed.
    Consider substrings of size m (m-grams)?
    The upper bound on possible decodings for a string of length n and 'unconstrained' m is nCm - m
      where nCm = n!/(m! . (n-m)!)
    :param use_cache: (optional) whether or not to use a cache during program execution (default: True)
    :param code_map: code dictionary mapping a str/char to an int
    :param code_str: code string
    :return: number of possible decodings
    """
    rev_map: RevMap = {}
    # reverse map, and extremal stats
    for key, item in code_map.items():
        rev_map[str(item)] = key
    # warm up cache
    cache: SetMap = {}
    if use_cache:
        for key in rev_map.keys():
            key_len = len(key)
            if key_len == 1:
                cache[key] = set(rev_map[key])
            if key_len == 2:
                if key[0] not in rev_map or key[1] not in rev_map:
                    cache[key] = set(rev_map[key])
                else:
                    cache[key] = set([rev_map[key[0]] + rev_map[key[1]], rev_map[key]])
    codewords = _find_codes(rev_map, cache, code_str)
    return len(codewords)


def _find_codes(rev_map: RevMap, cache: SetMap, code_str: str):
    """
    Solution should work even if the cache is empty.
    :param rev_map: reverse map
    :param cache: a cache that maps a code string to a set of all possible decoded strings
    :param code_str: code as string
    :return: a set of all possible decoded strings for given code string
    """
    if not code_str:
        return set()
    if code_str in cache:
        return cache[code_str]
    codewords = set()
    if code_str in rev_map:
        if len(code_str) == 1:
            return set(rev_map[code_str])
        codewords = set(rev_map[code_str])
    for idx in range(len(code_str) - 1):
        subcodes = _find_codes(rev_map, cache, code_str[idx + 1:])
        prefixes = _find_codes(rev_map, cache, code_str[0:idx + 1])

        # cross-product
        for prefix in prefixes:
            for subcode in subcodes:
                codewords.add(prefix + subcode)
    cache[code_str] = codewords
    # print(codewords)
    return codewords


if __name__ == "__main__":
    codes = "abcdefghijklmnopqrstuvwxyz"
    code_map = {codes[idx]: idx + 1 for idx in range(len(codes))}

    assert count(code_map, "11") == 2
    assert count(code_map, "111") == 3
    assert count(code_map, "11111") == 8
    assert count(code_map, "12121") == 8
    assert count(code_map, "22222") == 8
    assert count(code_map, "22227") == 5
    assert count(code_map, "7777777777") == 1

    assert count(code_map, "11", False) == 2
    assert count(code_map, "111", False) == 3
    assert count(code_map, "11111", False) == 8
    assert count(code_map, "12121", False) == 8
    assert count(code_map, "22222", False) == 8
    assert count(code_map, "22227", False) == 5
    assert count(code_map, "7777777777", False) == 1

    code_map = {'a': 1, 'b': 11, 'c': 111, 'd': 1111}
    assert count(code_map, "11") == 2
    assert count(code_map, "111") == 4
    assert count(code_map, "1111") == 8

    assert count(code_map, "11", False) == 2
    assert count(code_map, "111", False) == 4
    assert count(code_map, "1111", False) == 8
