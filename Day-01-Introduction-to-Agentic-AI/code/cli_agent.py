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
