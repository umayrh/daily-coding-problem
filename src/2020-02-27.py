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


def _find_longest_palindrome_substr1(s: str, s_len: int) -> (str, int, int):
    # Naive O(n^3) algo
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


def _find_longest_palindrome_substr(s: str, s_len: int) -> (str, int, int):
    # Runs in O(n^2) worst-case. Looks for AA or ABA patterns.
    # Can this be O(nlgn) is idx is incremented appropriately?
    longest = ""
    longest_st = -1
    longest_en = -1
    idx = 1
    while idx < s_len:
        if s[idx] == s[idx - 1]:
            st = idx - 1
            en = idx
        elif idx < s_len - 1 and s[idx - 1] == s[idx + 1]:
            st = idx - 1
            en = idx + 1
        else:
            idx += 1
            continue
        while st >= 0 and en < s_len and s[st] == s[en]:
            st -= 1
            en += 1
        st += 1
        en -= 1
        # can I get away with jumping the gun here?
        # idx = en
        if en - st > longest_en - longest_st:
            longest = s[st:en+1]
            longest_st = st
            longest_en = en
        # Amongst equals, select the palindrome bounded by the lexicographically smallest character
        # FIXME maybe not quite right since we're only looking at the immediate bounding chars, which may be equal
        elif en - st == longest_en - longest_st:
            st_p = st - 1 if st > 0 else 0
            en_p = en + 1 if en < s_len - 1 else s_len - 1
            longest_st_p = longest_st - 1 if longest_st > 0 else 0
            longest_en_p = longest_en + 1 if longest_en < s_len - 1 else s_len - 1
            if min(s[st_p], s[en_p]) < min(s[longest_st_p], s[longest_en_p]):
                longest = s[st:en+1]
                longest_st = st
                longest_en = en
        idx += 1
    print(f"{longest}, {longest_st}, {longest_en}")
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
    # Longest palindromic substring found
    if longest_st >= 0:
        # The substring prefixes the string
        if longest_st == 0:
            prefix = "".join([s[idx] for idx in range(s_len - 1, longest_en, -1)])
            suffix = s
        # The substring suffixes the string
        elif longest_en == s_len - 1:
            prefix = s
            suffix = "".join([s[idx] for idx in range(longest_st - 1, -1, -1)])
        # The substring straddles the middle
        else:
            prefix = s[:longest_st]
            suffix = s[longest_en + 1:]
            # Create lexicographically smallest prefix
            prefix = suffix + prefix if prefix > suffix else prefix + suffix
            # Suffix is prefix reversed appended to the longest palindromic substring
            suffix = longest + "".join([prefix[idx] for idx in range(len(prefix) - 1, -1, -1)])
        return prefix + suffix
    # No palindromic substring. Create lexicographically smallest palindrome.
    prefix = "".join([s[idx] for idx in range(s_len - 1, 0, -1)]) if s[0] >= s[s_len - 1] else s
    suffix = "".join([s[idx] for idx in range(s_len - 2, -1, -1)]) if s[0] < s[s_len - 1] else s
    return prefix + suffix


if __name__ == "__main__":
    assert make_palindrome("google") == "elgoogle"
    assert make_palindrome("race") == "ecarace"
    assert make_palindrome("elgoog") == "elgoogle"
    assert make_palindrome("elgoogle") == "elgoogle"
    assert make_palindrome("lgooge") == "elgoogle"
    assert make_palindrome("mommy") == "ymmommy"
    assert make_palindrome("ooooooomooooooo1") == "1ooooooomooooooo1"
    assert make_palindrome("mommommom") == "mommommom"
    assert make_palindrome("1mommommom") == "1mommommom1"
    assert make_palindrome("abcxxdefyyghizz") == "abcdefyyghizzxxzzihgyyfedcba"
    assert make_palindrome("ghixxdefyyabczz") == "abczzghixxdefyyfedxxihgzzcba"
