"""
Given a string and a set of delimiters, reverse the words in the string while maintaining the
relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

def reverse(phrase, delimiters):
    words = phrase.split(delimiters)
    delim_idx = 0
    delim_queue = []
    for word in words:
        delim_idx = delim_idx + len(word)
        delim_queue.append(phrase[delim_idx])

    result = ""
    delim_idx = 0
    if phrase[0] in delimiters:
        result += delim_queue[delim_idx]
        delim_idx += 1
    for word_idx in range(len(words):
        word = words[-word_idx]
        if delim_idx < len(delim_queue):
            result += delim_queue[delim_idx]
            delim_idx += 1
     return result


if __name__ == "__main__":
    assert reverse("hello/world:here") == "here/world:hello"
    assert reverse("hello/world:here/") == "here/world:hello/"
    assert reverse("hello//world:here") == "here//world:hello"
