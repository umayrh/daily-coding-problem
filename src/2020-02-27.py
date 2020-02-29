"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters
as possible anywhere in the word. If there is more than one palindrome of minimum length that
can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters
to it (which is the smallest amount to make a palindrome). There are seven other palindromes
that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""


def _is_palindrome(s: str) -> bool:
    s_len = len(s)
    for idx in range(int(s_len / 2)):
        if s[idx] != s[s_len - 1 - idx]:
            return False
    return True


def _find_longest_palindrome_substr(s: str, s_len: int) -> (str, int, int):
    # TODO do it in O(n) by looking at AA or ABA patterns
    longest = ""
    longest_st = -1
    longest_en = -1
    for st in range(s_len - 1):
        for en in range(st + 1, s_len):
            substr = s[st:en+1]
            if _is_palindrome(substr) and len(substr) > len(longest):
                longest = substr
                longest_st = st
                longest_en = en
    return longest, longest_st, longest_en


def make_palindrome(s: str) -> str:
    if not str:
        return ""
    s_len = len(s)
    if s_len < 2:
        return s + "" + s
    # Find the longest palindrome, if any
    longest, longest_st, longest_en = _find_longest_palindrome_substr(s, s_len)
    # Entire string is a palindrome
    if longest_st == 0 and longest_en == s_len - 1:
        return s
    # Palindromic substring found
    if longest_st >= 0:
        prefix = "".join([s[idx] for idx in range(s_len - 1, longest_en, -1)]) if longest_st == 0 else s
        suffix = "".join([s[idx] for idx in range(longest_st - 1, -1, -1)]) if longest_st > 0 else s
        print(f"{prefix} {suffix} {longest_st} {longest_en}")
        return prefix + suffix
    # No palindromic substring. Create lexicographically smallest palindrome.
    prefix = "".join([s[idx] for idx in range(s_len - 1, 0, -1)]) if s[0] >= s[s_len - 1] else s
    suffix = "".join([s[idx] for idx in range(s_len - 2, -1, -1)]) if s[0] < s[s_len - 1] else s
    print(f"{prefix} {suffix} {longest_st} {longest_en}")
    return prefix + suffix


if __name__ == "__main__":
    assert make_palindrome("google") == "elgoogle"
    assert make_palindrome("race") == "ecarace"
    assert make_palindrome("elgoog") == "elgoogle"
    assert make_palindrome("elgoogle") == "elgoogle"
    assert make_palindrome("mommy") == "ymmommy"

