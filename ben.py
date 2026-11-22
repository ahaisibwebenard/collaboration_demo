"""Basic arithmetic operations and operator dispatch."""

from collections.abc import Callable
from numbers import Real

Operation = Callable[[Real, Real], Real]


def add(a: Real, b: Real) -> Real:
    return a + b


def subtract(a: Real, b: Real) -> Real:
    return a - b


def multiply(a: Real, b: Real) -> Real:
    return a * b


def divide(a: Real, b: Real) -> Real:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


_OPERATIONS: dict[str, Operation] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a: Real, operation: str, b: Real) -> Real:
    """Calculate an arithmetic operation.

    Raises:
        ValueError: If the operation is unsupported or division is by zero.
    """
    try:
        return _OPERATIONS[operation](a, b)
    except KeyError:
        raise ValueError(f"Invalid operation: {operation!r}") from None
