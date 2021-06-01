"""
Register mathematical functions using decorators.
"""
import functools
import re

FUNCTIONS = {}
RE_OPERATION = re.compile(r"\((?P<operation>\w+) (?P<v1>\d+) (?P<v2>\d+)\)")


def register(func):

    @functools.wraps(func)
    def wrapped(v1: int, v2: int) -> int:
        result = func(v1, v2)

        print(f"result: {result}")

        return result

    FUNCTIONS[func.__name__] = wrapped
    return wrapped


@register
def add(v1: int, v2: int) -> int:
    return v1 + v2


@register
def sub(v1: int, v2: int) -> int:
    return v1 - v2


@register
def mul(v1: int, v2: int) -> int:
    return v1 * v2


@register
def div(v1: int, v2: int) -> int:
    return v1 / v2


def compute(expression: str) -> int:
    """Compute a Polish Notation expression."""
    m = RE_OPERATION.match(expression)
    operation, v1, v2 = m.group("operation"), int(m.group("v1")), int(m.group("v2"))
    return FUNCTIONS[operation](v1, v2)


def test_compute() -> None:
    assert compute("(add 1 2)") == 3
    assert compute("(mul 1 2)") == 2
    assert compute("(div 4 2)") == 2
    assert compute("(sub 5 2)") == 3


if __name__ == "__main__":
    test_compute()
