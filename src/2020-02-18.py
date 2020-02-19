"""
Implement regular expression matching with the following special characters:

* `.` (period) which matches any single character
* `*` (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns
whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return
true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
"""


def matches(regex: str, word: str) -> bool:
    if not regex:
        return False
    curr_idx = 0
    prev_star_substr = ""
    for star_substr in regex.split("*"):
        if not star_substr:
            continue
        prev_dot_idx = 0
        # Looks for zero or more matchings of the preceding element
        if prev_star_substr and prev_star_substr[-1] != ".":
            while star_substr[prev_dot_idx] == prev_star_substr[-1]:
                curr_idx = curr_idx + 1
                prev_dot_idx = prev_dot_idx + 1
        next_dot_idx = star_substr.find(".", prev_dot_idx)
        if next_dot_idx < prev_dot_idx:
            next_dot_idx = len(star_substr)
        while prev_dot_idx <= next_dot_idx:
            if next_dot_idx < prev_dot_idx:
                next_dot_idx = len(star_substr)
            # Dot is the first char in substr
            elif next_dot_idx == prev_dot_idx:
                if curr_idx >= len(word):
                    return False
                curr_idx = curr_idx + 1
            else:
                dot_substr = star_substr[prev_dot_idx:next_dot_idx]
                substr_idx = word.find(dot_substr, curr_idx)
                if substr_idx < curr_idx:
                    return False
                curr_idx = substr_idx + next_dot_idx - prev_dot_idx
                if next_dot_idx < len(star_substr):
                    curr_idx = curr_idx + 1
            prev_dot_idx = next_dot_idx + 1
            next_dot_idx = star_substr.find(".", prev_dot_idx)
        prev_star_substr = star_substr
        # print(f"{regex}, {word}: {curr_idx}")
    if curr_idx < len(word) and regex[-1] != "*":
        return False
    return True


if __name__ == "__main__":
    assert matches("ra.", "ray") is True
    assert matches("ra.", "raymond") is False
    assert matches(".*at", "chat") is True
    assert matches(".*at", "chats") is False

    assert matches("*", "") is True
    assert matches("*******", "") is True
    assert matches(".", "") is False
    assert matches(".*", "") is False
    assert matches(".", "a") is True
    assert matches(".", "aa") is False
    assert matches("..", "aa") is True
    assert matches(".*", "a") is True
    assert matches(".*", "aaa") is True

    assert matches("*abc", "abc") is True
    assert matches("ab*c", "abc") is True
    assert matches("abc*", "abc") is True
    assert matches("a*b*c*", "abc") is True
    assert matches("*abc", "abcd") is False
    ### is this correct?
    assert matches("*abc**", "abcccccd") is True
