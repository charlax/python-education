"""
Register mathematical functions using decorators.

We also want to log the result of all operations.

To test your solution, run `pytest -s` on it.

To go further:

- Allow registering a function using an alias to allow "(+ 1 2)"
"""


# @register
def mul(v1: int, v2: int) -> int:
    return v1 * v2


def compute(expression: str) -> int:
    """Compute a Polish Notation expression."""
    return 0


def test_compute() -> None:
    assert compute("(add 1 2)") == 3
    assert compute("(mul 1 2)") == 2
    assert compute("(div 4 2)") == 2
    assert compute("(sub 5 2)") == 3


if __name__ == "__main__":
    test_compute()
