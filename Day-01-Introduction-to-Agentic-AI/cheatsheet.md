# Day 01 — Cheat Sheet: Agent Fundamentals

## The Loop
```
PERCEIVE -> REASON -> ACT -> OBSERVE -> (repeat) -> RESPOND
```

## Levels of Agency (quick reference)
| Level | Capability |
|---|---|
| 0 | Plain LLM call, no tools |
| 1 | Single tool |
| 2 | Multiple tools + short-term memory |
| 3 | Planning + multi-step autonomy |
| 4 | Multi-agent delegation |

## Minimal Tool Definition Template
```python
def my_tool(arg1: str) -> str:
    """One-line description of what this tool does."""
    # ... do the thing
    return "result as a string"

TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "my_tool",
        "description": "What this tool does and when to use it",
        "parameters": {
            "type": "object",
            "properties": {"arg1": {"type": "string", "description": "..."}},
            "required": ["arg1"],
        },
    },
}
```

## Non-Negotiable Safety Rules
- Always set `max_steps` / a loop bound
- Never `eval()` untrusted input without sandboxing
- Always feed tool errors back as observations, don't swallow them
- Log every tool call (name, args, result, timestamp)

## Key Terms
- **Orchestrator** — the code that runs the loop
- **Observation** — the result of an action, fed back to the LLM
- **Grounding** — giving the LLM real data instead of letting it guess
