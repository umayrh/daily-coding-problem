"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

from typing import Dict
Map = Dict[str, str]


def longest_substring3(s: str, k: int):
    strlen = len(s)
    if len(set(s)) < k:
        return ""
    st = 0
    en = 0
    max_len = 0
    result = ""
    base_set = set()
    for idx in range(strlen):
        prev_base = base_set
        base_set = base_set.union(s[idx])
        base_len = len(base_set)
        if base_len < k:
            en = en + 1
        elif base_len == k:
            en = en + 1
            if en - st > max_len:
                max_len = en - st
                result = s[st:en]
        else:
            prev = idx - 1
            # TODO figure out the longest substring ending at idx-1 with k-1 unique chars
    return result


def longest_substring2(s: str, k: int):
    strlen = len(s)
    if len(set(s)) < k:
        return ""
    idx = 0
    max_len = 0
    result = ""
    while idx < strlen - k:
        substr = s[idx:idx+k]
        substr_set = set(substr)
        uniq_len = len(substr_set)
        if uniq_len == k:
            result = substr if not result else result
            forw = idx + k
            while forw < strlen - 1 and s[forw] in substr_set:
                forw = forw + 1
            forw_len = forw - idx
            if forw_len > max_len:
                max_len = forw_len
                result = s[idx:forw]
                print(result)
                idx = forw
            # TODO figure out how to avoid unnecessary reverse lookups
            revr = idx
            while 0 <= revr < idx and s[revr] in substr_set:
                revr = revr - 1
            revr_len = idx + k - revr
            if revr_len > max_len:
                max_len = revr_len
                result = s[revr:idx+k]
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
