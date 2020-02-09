"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

from typing import Dict
Map = Dict[str, str]

"""
MAX(l)
s.t.
str(s, e) = str(s, m) + str(m + 1, e)
|str(s, m) U str(m + 1, e)| = k
e - s + 1 = l

if len(set(s)) <= k
  return s

for idx in range(k, strlen):
    prefix = func(
The longest substring ending at idx-1 with k-1 unique chars
"""


def longest_substring3(s: str, k: int):
    cache = {}
    _longest_substring3(s, k, 0, set(), cache)
    print(cache)


def _longest_substring3(s: str, k: int, st: int, exclude: set, cache: dict):
    strlen = len(s)
    s_set = set(s)
    s_set_len = len(s_set)
    is_disjoint = s_set.isdisjoint(exclude)
    if s_set_len < k or not is_disjoint:
        return ""
    if s_set_len == k and is_disjoint:
        return s
    if st in cache:
        return cache[st]
    max_result = ""
    for idx in range(st, strlen):
        prefix = s[idx]
        suffix1 = _longest_substring3(s[idx + 1:], k - 1, st + 1, exclude.union(set(prefix)), cache)
        suffix2 = _longest_substring3(s[idx + 1:], k, st + 1, exclude, cache)
        suffix = suffix2 if len(suffix2) > len(suffix1) else suffix1
        suffix_len = len(suffix)
        result = prefix + suffix
        if idx in cache:
            if len(cache[idx]) > suffix_len + 1:
                cache[idx] = prefix + suffix
            else:
                result = cache[idx]
        else:
            cache[idx] = prefix + suffix
        print(f"{idx}: {s}: {suffix1}, {suffix2}")
        if len(result) > len(max_result):
            max_result = result
    return max_result


def longest_substring2(s: str, k: int):
    strlen = len(s)
    if len(set(s)) < k:
        return ""
    st = 0
    en = k
    idx = 0
    max_len = 0
    result = ""
    while en <= strlen - k:
        substr = s[st:en]
        substr_set = set(substr)
        uniq_len = len(substr_set)
        if uniq_len == k:
            while en < strlen and s[en] in substr_set:
                en = en + 1
            forw_len = en - st
            if forw_len > max_len:
                max_len = forw_len
                result = s[st:en]
                print(result)
                # st is the start of  substr with k-1 uniq chars
                st = en
                en = st + k
        else:
            while en < strlen - 1 and s[en] in substr_set:
                en = en + 1
        idx = idx + 1
    return result


def longest_substring1(s: str, k: int):
    strlen = len(s)
    if len(set(s)) < k:
        return ""
    max_len = 0
    result = ""
    for st_idx in range(0, strlen - k):
        for en_idx in range(st_idx + k, strlen + 1):
            substr = s[st_idx:en_idx]
            uniq_len = len(set(substr))
            if uniq_len == k:
                if len(substr) > max_len:
                    max_len = len(substr)
                    result = substr
    return result


if __name__ == "__main__":
    assert longest_substring1("abcba", 2) == "bcb"
    assert longest_substring1("bbbbbbbba", 2) == "bbbbbbbba"
    assert longest_substring1("abcdef", 2) == "ab"
    assert longest_substring1("aaaaaaa", 2) == ""
    assert longest_substring1("abcbcbcdcdcdcdc", 3) == "bcbcbcdcdcdcdc"

    longest_substring3("abcba", 2)
