"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
repeated successive characters as a single count and character. For example, the string
"AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits
and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""


def encode(plaintext: str):
    text_len = len(plaintext)
    if text_len == 0:
        return ""
    if text_len == 1:
        return f"1{plaintext}"
    count = 1
    code = ""
    prev = plaintext[0]
    for idx in range(1, text_len):
        if plaintext[idx] == prev:
            count = count + 1
        else:
            code = code + str(count) + plaintext[idx - 1]
            prev = plaintext[idx]
            count = 1
    return code + str(count) + plaintext[-1]


def decode(code: str):
    code_len = len(code)
    if code_len == 0:
        return ""
    result = ""
    for idx in range(0, code_len - 1, 2):
        result = result + code[idx + 1] * int(code[idx])
    return result


if __name__ == "__main__":
    assert decode(encode("AAAABBBCCDAA")) == "AAAABBBCCDAA"
    assert encode(decode("1X2Y3Z")) == "1X2Y3Z"
    assert encode(decode("5 ")) == "5 "
