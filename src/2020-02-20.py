"""
Given a string of round, curly, and square open and closing brackets, return whether the
brackets are balanced (well-formed).

For example, given the string `"([])[]({})"`, you should return true.

Given the string `"([)]"` or `"((()"`, you should return false.
"""


def balanced(brackets: str) -> bool:
    stack = list()
    for idx in range(len(brackets)):
        for st, en in [("(", ")"), ("{", "}"), ("[", "]")]:
            if brackets[idx] == st:
                stack.append(brackets[idx])
            elif brackets[idx] == en:
                if stack.pop() != st:
                    return False
    return len(stack) == 0


if __name__ == "__main__":
    assert balanced("([])[]({})") is True
    assert balanced("([)]") is False
    assert balanced("((()") is False

    assert balanced("(((]]]") is False
    assert balanced("((({)))") is False
    assert balanced("((({])))") is False
    assert balanced("((({})))") is True
    assert balanced("[({([])[]({})})]") is True
