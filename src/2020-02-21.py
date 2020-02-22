"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a
list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least
one space between each word. Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed
starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words `["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy",
"dog"]` and k = 16, you should return the following:

```
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```
"""
from typing import List
Text = List[str]


def _justify(words: Text, line_len: int, k: int) -> str:
    """
    Justifies a list of words with a line length < k
    :param words: list of strings
    :param line_len: total number of characters in the list (so, excludes padding)
    :param k: max length of a line
    :return: `str` as justified text
    """
    # If you can only fit one word on a line, then you should pad the right-hand side.
    num_words = len(words)
    if num_words == 1:
        return words[0] + " " * (k - len(words[0]))
    # Spaces should be distributed as equally as possible, with the extra spaces,
    # if any, distributed starting from the left.
    num_spaces = k - line_len
    spaces_per_word = int(num_spaces / (num_words - 1))
    spaces_left = num_spaces % (num_words - 1)
    justified_line = words[0]
    for idx in range(1, num_words):
        word = words[idx]
        pad_len = spaces_per_word
        if spaces_left > 0:
            pad_len = pad_len + 1
            spaces_left = spaces_left - 1
        justified_line = justified_line + " " * pad_len + word
    return justified_line


def justify(text: Text, k: int) -> str:
    if not text or k <= 0:
        return ""
    justified = list()
    word_idx_st = 0
    word_idx_en = 0
    line_len = 0
    for word in text:
        word_len = len(word)
        pad_len = 1 if word_len > 0 else 0
        line_len = line_len + word_len + pad_len
        if word_len >= k - 1:
            justified.append(word + " "[0:pad_len])
            line_len = 0
            word_idx_st = word_idx_en + 1
        elif line_len == k + pad_len:
            subtext = text[word_idx_st:word_idx_en + 1]
            num_words = word_idx_en + 1 - word_idx_st
            justified_line = _justify(subtext, line_len - num_words, k)
            justified.append(justified_line)
            line_len = 0
            word_idx_st = word_idx_en + 1
        elif line_len > k + pad_len:
            subtext = text[word_idx_st:word_idx_en]
            num_words = word_idx_en - word_idx_st
            justified_line = _justify(subtext, line_len - num_words - word_len - pad_len, k)
            justified.append(justified_line)
            line_len = word_len + pad_len
            word_idx_st = word_idx_en
        word_idx_en = word_idx_en + 1
    if line_len > 0:
        subtext = text[word_idx_st:word_idx_en]
        num_words = word_idx_en - word_idx_st
        justified_line = _justify(subtext, line_len - num_words, k)
        justified.append(justified_line)
    return justified


if __name__ == "__main__":
    text = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    result = justify(text, 16)
    assert result == ["the  quick brown", "fox  jumps  over", "the   lazy   dog"], result

    result = justify(text, 10)
    assert result == ["the  quick", "brown  fox", "jumps over", "the   lazy", "dog       "], result
