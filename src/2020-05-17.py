"""
Given a string and a set of delimiters, reverse the words in the string while maintaining the
relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""
import re


def reverse(phrase, delimiters):
    words = re.split(delimiters, phrase)
    if '' in words:
        words.remove('')

    delim_queue = []
    delim_st = 0
    phrase_len = len(phrase)
    for idx in range(len(words)):
        delim_en = phrase.find(words[idx], delim_st, phrase_len)
        delim_queue.append(phrase[delim_st:delim_en])
        delim_st = delim_en + len(words[idx])
    delim_queue.append(phrase[delim_st:phrase_len])

    delim_idx = 1
    result = delim_queue[0]
    for word_idx in range(len(words)):
        result += words[-word_idx-1]
        if delim_idx < len(delim_queue):
            result += delim_queue[delim_idx]
            delim_idx += 1
    return result


if __name__ == "__main__":
    assert reverse("hello/world:here", "/|:") == "here/world:hello"
    assert reverse("hello/world:here/", "/|:") == "here/world:hello/"
    assert reverse("hello//world:here", "//|:") == "here//world:hello"
