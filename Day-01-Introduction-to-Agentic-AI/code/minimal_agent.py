"""
A minimal agent loop, framework-free.
Demonstrates: perceive -> reason -> act -> observe -> respond
"""

import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def calculator(expression: str) -> str:
    """Safely evaluate a basic arithmetic expression."""
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
                    "expression": {
                        "type": "string",
                        "description": "A valid arithmetic expression",
                    }
                },
                "required": ["expression"],
            },
        },
    }
]

AVAILABLE_FUNCTIONS = {"calculator": calculator}


def run_agent(user_goal: str, max_steps: int = 5) -> str:
    """The core agent loop: reason -> act -> observe -> repeat."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a careful assistant. Use the calculator tool for any "
                "arithmetic instead of computing it yourself."
            ),
        },
        {"role": "user", "content": user_goal},
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
        )
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for tool_call in msg.tool_calls:
                fn_name = tool_call.function.name
                fn_args = json.loads(tool_call.function.arguments)

                print(f"[step {step}] Agent calls {fn_name}({fn_args})")

                result = AVAILABLE_FUNCTIONS[fn_name](**fn_args)

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )
            continue

        return msg.content

    return "Max steps reached without a final answer."


if __name__ == "__main__":
    goal = "What is (482 * 17) - 96, and then explain briefly why agents need tools for math?"
    answer = run_agent(goal)
    print("\n--- FINAL ANSWER ---")
    print(answer)
