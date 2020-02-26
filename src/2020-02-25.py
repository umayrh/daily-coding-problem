"""
The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other. For example,
the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”,
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
from typing import List
Vector = List[int]


def edit_distance(str1: str, str2: str) -> int:
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    str1_len = len(str1)
    str2_len = len(str2)
    shorter = str1 if str1_len < str2_len else str2
    shorter_len = min(str1_len, str2_len)
    longer = str2 if str1_len < str2_len else str1
    longer_len = max(str1_len, str2_len)
    longer_st = 0
    max_matches = 0
    # find the alignment with maximum matchings
    for st in range(longer_len - shorter_len + 1):
        matches = 0
        for idx in range(shorter_len):
            if shorter[idx] == longer[st + idx]:
                matches += 1
        if matches > max_matches:
            max_matches = matches
            longer_st = st
    # count mis-alignments
    distance = longer_st
    for idx in range(longer_st, len(longer)):
        if idx - longer_st < shorter_len:
            if shorter[idx - longer_st] != longer[idx]:
                distance += 1
        else:
            distance += 1
    return distance


if __name__ == "__main__":
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("abcxyz", "xyz") == 3
    assert edit_distance("abcxyz", "pqr") == 6
    assert edit_distance("mississippi", 'missouri') == 6
