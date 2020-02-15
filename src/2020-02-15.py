"""
Given a dictionary of words and a string made up of those words (no spaces), return the original
sentence in a list. If there is more than one possible reconstruction, return any of them. If there
is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
from typing import Set
Dict = Set[str]


def _possible_words(dictionary: Dict, st_idx: int, words: str) -> (Dict, int):
    if not words or st_idx < 0 or st_idx >= len(words):
        return set(), st_idx
    if words in dictionary:
        return {words}, st_idx + len(words)
    elif len(words) <= 2:
        return set(), st_idx
    # return the first (hence shortest matching word) in the dict
    for idx in range(st_idx+2, len(words) + 1):
        word = words[st_idx:idx]
        if word in dictionary:
            return {word}, idx
    return set(), st_idx


def possible_words(dictionary: Dict, words: str) -> Dict:
    result = set()
    idx = 0
    while idx < len(words):
        word_set, en_idx = _possible_words(dictionary, idx, words)
        if word_set:
            result = result.union(word_set)
            idx = en_idx
        else:
            idx = idx + 1
    return result


if __name__ == "__main__":
    result = possible_words({'quick', 'brown', 'the', 'fox'}, "thequickbrownfox")
    assert result == {'the', 'quick', 'brown', 'fox'}, result
    result = possible_words({'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond")
    assert result == {'bed', 'bath', 'and', 'beyond'} or result == {'bedbath', 'and', 'beyond'}, result
