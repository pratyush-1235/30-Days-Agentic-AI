# Day 01 — Mini Project: "Ask-and-Calculate" CLI Agent

## Project Requirements

Build a small command-line agent that:
1. Accepts a user question via terminal input (a loop, not just one-shot)
2. Uses the calculator tool from the lesson for any arithmetic
3. Maintains conversation history across multiple turns in the same session
4. Exits cleanly when the user types `exit` or `quit`
5. Logs every tool call to the console with a timestamp

## Folder Structure

```
Day-01-Introduction-to-Agentic-AI/
└── code/
    ├── minimal_agent.py     # from the lesson
    ├── cli_agent.py         # this project
    └── tools.py             # shared tool definitions
```

## Implementation

`code/tools.py`:
```python
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
```

`code/cli_agent.py`:
```python
"""
Day 1 Mini Project: Ask-and-Calculate CLI Agent.
A persistent terminal chat loop with tool-calling and history.
"""

import json
import os
from datetime import datetime
from openai import OpenAI
from tools import TOOLS, AVAILABLE_FUNCTIONS

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are a helpful assistant. Use the calculator tool for any arithmetic "
    "instead of computing it yourself. Keep answers concise."
)


def log_tool_call(name: str, args: dict, result: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] TOOL CALL -> {name}({args}) = {result}")


def run_turn(messages: list, max_steps: int = 5) -> str:
    for _ in range(max_steps):
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages, tools=TOOLS
        )
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for tool_call in msg.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                result = AVAILABLE_FUNCTIONS[name](**args)
                log_tool_call(name, args, result)
                messages.append(
                    {"role": "tool", "tool_call_id": tool_call.id, "content": result}
                )
            continue

        return msg.content

    return "I've reached my step limit for this turn — try rephrasing your question."


def main():
    print("CLI Agent ready. Type 'exit' or 'quit' to stop.\n")
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        reply = run_turn(messages)
        messages.append({"role": "assistant", "content": reply})
        print(f"Agent: {reply}\n")


if __name__ == "__main__":
    main()
```

## Testing

`tests/test_cli_agent.py`:
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from tools import calculator

def test_calculator_basic():
    assert calculator("2 + 2") == "4"

def test_calculator_division_by_zero():
    assert calculator("1 / 0") == "Error: division by zero"

def test_calculator_rejects_code_injection():
    result = calculator("__import__('os').system('ls')")
    assert result.startswith("Error")
```

Run with:
```bash
cd Day-01-Introduction-to-Agentic-AI
pytest tests/ -v
```

## Expected Output

```
CLI Agent ready. Type 'exit' or 'quit' to stop.

You: what's 14 squared plus 9?
[14:02:11] TOOL CALL -> calculator({'expression': '14**2 + 9'}) = 205
Agent: 14 squared plus 9 is 205.

You: exit
Goodbye!
```

## Improvements

- Persist conversation history to disk (JSON) so sessions can resume
- Add a `/reset` command to clear history mid-session
- Stream responses token-by-token instead of waiting for the full completion
- Add a second tool (unit converter, date calculator) to practice multi-tool selection

## Bonus Challenges

1. Add a `--model` CLI flag (using `argparse`) to switch between models at launch.
2. Add color-coded terminal output (e.g., using `rich`) distinguishing user input,
   agent replies, and tool-call logs.
3. Add a `/history` command that prints the full conversation so far.
