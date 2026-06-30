"""Shared tool definitions for Day 1 project."""


def calculator(expression: str) -> str:
    allowed_chars = set("0123456789+-*/(). ")
    if not set(expression) <= allowed_chars:
        return "Error: invalid characters in expression"
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except ZeroDivisionError:
        return "Error: division by zero"
    except Exception as e:
        return f"Error: {e}"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic arithmetic expression, e.g. '12 * (3 + 4)'",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "A valid arithmetic expression"}
                },
                "required": ["expression"],
            },
        },
    }
]

AVAILABLE_FUNCTIONS = {"calculator": calculator}
