"""
`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of
that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement `car` and `cdr`.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def _pair(a, b):
    return a, b


def car(pair):
    return pair(_pair)[0]


def cdr(pair):
    return pair(_pair)[1]


if __name__ == "__main__":
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
