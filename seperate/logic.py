def evaluate_expression(expression: str) -> str:
    """Safely evaluate a full math expression."""
    try:
        result = str(eval(expression))
        return result
    except Exception:
        return "Error"


def square(value: str) -> str:
    """Return square of a number (as string)."""
    try:
        return str(eval(f"{value}**2"))
    except Exception:
        return "Error"


def sqrt(value: str) -> str:
    """Return square root of a number (as string)."""
    try:
        return str(eval(f"{value}**0.5"))
    except Exception:
        return "Error"
