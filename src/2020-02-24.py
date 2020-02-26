"""
The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other. For example,
the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”,
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
from typing import List
Vector = List[int]


def _str_to_map(s: str) -> dict:
    res = {}
    for idx in range(len(s)):
        if s[idx] in res:
            res[s[idx]] += 1
        else:
            res[s[idx]] = 1
    return res


def edit_distance(str1: str, str2: str) -> int:
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    map1 = _str_to_map(str1)
    map2 = _str_to_map(str2)

    common_chars = set(map1.keys()).intersection(set(map2.keys()))
    for char in common_chars:
        if map2[char] > map1[char]:
            map2[char] -= map1[char]
            map1[char] = 0
        else:
            map1[char] -= map2[char]
            map2[char] = 0
    dist = max(sum(map1.values()), sum(map2.values()))

    # check for anagrams
    if dist == 0:
        mismatches = 0
        for idx in range(len(str1)):
            if str1[idx] != str2[idx]:
                mismatches += 1
        dist = mismatches
    return dist


if __name__ == "__main__":
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("abcxyz", "xyz") == 3
    assert edit_distance("abcxyz", "pqr") == 6
    assert edit_distance("mississippi", 'missouri') == 6
    assert edit_distance("lope", "pole") == 2
