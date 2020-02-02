"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
from math import log10
from typing import Dict
CodeMap = Dict[str, int]
RevMap = Dict[str, str]
SetMap = Dict[str, set]


def count(code_map: CodeMap, code_str: str):
    """
    Find, m, the max characters in the mapping. Here, 2
    The upper bound on possible decodings for a string of length n and 'unconstrained' m is nCm - m
      where nCm = n!/(m! . (n-m)!)
    For example:
      111111=aaaaaa,kaaaa,akaaa,aakaa,aaaka,aaaak,kkaa,kaka,kaak,akka,aakk,akak,kkk (6x5/2 - 2 = 13)
      22222=,bbbbb,vbbb,bvbb,bbvb,bbbv,vvb,vbv,bvv (5x4/2 - 2 = 8)
      22227=bbbbg,vbbg,bvbg,bbvg,vvg (4x3/2 - 2 = 4 != 5...?)
      1111=aaaa,kaa,aka,aak,kk
      abcd = ab.cd, ac.bd, ad.bc, bc.ad, bd.ca, cd.ad
      111=aaa,ak,ka (3x2/2 - 2 = 1 != 3...?)
    Assuming for now the mapping contains a contiguous set of ints?
    Consider substrings of size m (m-grams)?
    :param code_map: code dictionary mapping a str/char to an int
    :param code_str: code string
    :return: number of possible decodings
    """
    max_code_chr_len: int = 0
    rev_map: RevMap = {}
    cache: SetMap = {}
    # reverse map, and extremal stats
    for key, item in code_map.items():
        max_code_chr_len = max(max_code_chr_len, int(log10(item)) + 1)
        rev_map[str(item)] = key
    # warm up cache
    for key in rev_map.keys():
        if len(key) == 2:
            if key[0] not in rev_map or key[1] not in rev_map:
                cache[key] = set(rev_map[key])
            else:
                cache[key] = set([rev_map[key[0]] + rev_map[key[1]], rev_map[key]])
        else:
            cache[key] = set(rev_map[key])
    codewords = _find_codes(max_code_chr_len, rev_map, cache, code_str)
    print(codewords)
    return len(codewords)


def _find_codes(max_code_chr_len: int, rev_map: RevMap, cache: SetMap, code_str: str):
    # aaaa -> aa(k, aa), k(k, aa), a(ka, ak)
    if not code_str:
        return set("")
    if code_str in cache:
        return cache[code_str]
    if code_str in rev_map:
        # not quite correct
        mapped = "".join([rev_map[code_str[idx]] for idx in range(len(code_str))])
        return set([mapped, rev_map[code_str]])
    codewords = set()
    for idx in range(len(code_str) - 1):
        subcodes = _find_codes(max_code_chr_len, rev_map, cache, code_str[idx + 1:])
        print(f"idx {idx}, {code_str}: subcodes: {subcodes}")
        prefix_idx = idx - max_code_chr_len + 1 if idx >= max_code_chr_len - 1 else idx
        prefixes = _find_codes(max_code_chr_len, rev_map, cache, code_str[prefix_idx:idx + 1])
        print(f"idx {idx}, {code_str}: prefixes: {prefixes}")
        # cross-product
        for prefix in prefixes:
            for subcode in subcodes:
                codewords.add(prefix + subcode)
        print(f"idx {idx}, {code_str}: codewords: {codewords}")
    cache[code_str] = codewords
    return codewords


if __name__ == "__main__":
    codes = "abcdefghijklmnopqrstuvwxyz"
    code_map = {codes[idx]: idx + 1 for idx in range(len(codes))}
    #assert count(code_map, "11") == 2
    #assert count(code_map, "111") == 3
    assert count(code_map, "11111") == 8
