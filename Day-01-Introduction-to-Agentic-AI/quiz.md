# Day 01 — Quiz

## Multiple Choice (10)

1. What primarily distinguishes an "agent" from a plain LLM call?
   a) The agent uses a bigger model
   b) The agent runs in a loop that can act, observe, and decide next steps
   c) The agent always uses LangChain
   d) The agent never makes mistakes
   **Answer: b**

2. In the perceive-reason-act-observe loop, what comes immediately after a tool is called?
   a) The loop terminates
   b) The result is observed and fed back into context
   c) The user is asked for confirmation
   d) The model is retrained
   **Answer: b**

3. Which of these is NOT one of the five core components discussed today?
   a) Planner
   b) Orchestrator
   c) Memory
   d) Compiler
   **Answer: d**

4. At which "Level of Agency" does a system have multiple tools and short-term memory, but no autonomous multi-step planning?
   a) Level 0
   b) Level 1
   c) Level 2
   d) Level 4
   **Answer: c**

5. Why does `minimal_agent.py` use `max_steps`?
   a) To save disk space
   b) To bound the loop and prevent runaway execution/cost
   c) It's required by the OpenAI API
   d) To slow down the response for readability
   **Answer: b**

6. What should happen when a tool call returns an error?
   a) The program should crash immediately
   b) The error should be silently ignored
   c) The error should be fed back to the model as an observation
   d) The agent should restart from scratch
   **Answer: c**

7. Which task is the best example of Level 3 agency?
   a) Translating a sentence
   b) Calling a single calculator tool once
   c) Autonomously planning and executing a multi-step research report with self-correction
   d) Returning a static FAQ answer
   **Answer: c**

8. In our code example, what data type does `calculator()` return?
   a) int
   b) float
   c) str
   d) dict
   **Answer: c**

9. Why shouldn't an LLM be trusted to compute exact arithmetic itself?
   a) LLMs are not allowed to do math by policy
   b) LLMs predict likely tokens, not guaranteed-correct calculations
   c) Math tokens cost more
   d) It's technically impossible for an LLM to output numbers
   **Answer: b**

10. What is the purpose of the `TOOLS` JSON Schema list in the example?
    a) It stores conversation history
    b) It describes available tools/functions so the LLM knows how to call them
    c) It's the system prompt
    d) It logs errors
    **Answer: b**

## Short Answer (5)

11. In 2-3 sentences, explain the difference between Level 1 and Level 2 agency.
12. Why is it important to keep tools "narrow" (doing one thing well) rather than broad and multi-purpose?
13. What would happen to `minimal_agent.py` if `max_steps` were removed entirely? Describe a realistic failure scenario.
14. Name one real product/use case from the lesson and explain which core components (LLM, tools, memory, planner, orchestrator) it most likely relies on.
15. Why is understanding the raw, framework-free agent loop valuable before learning LangChain/LangGraph?

## Coding Questions (5)

16. Write a tool function `is_prime(n: int) -> bool` and the corresponding JSON Schema entry for `TOOLS`.
17. Modify `run_agent()` to print the total number of tool calls made by the end of the run.
18. Write a guard clause that stops the agent loop early (before `max_steps`) if the same tool is called with identical arguments twice in a row.
19. Add a `try/except` around the OpenAI API call in `run_agent()` so a network failure returns `"Error: could not reach the model"` instead of crashing.
20. Write a unit test (pytest) for `calculator()` that checks both a valid expression and a rejected invalid-character expression.

### Answers to Coding Questions

```python
# 16.
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# JSON Schema entry:
{
    "type": "function",
    "function": {
        "name": "is_prime",
        "description": "Check whether an integer is prime",
        "parameters": {
            "type": "object",
            "properties": {"n": {"type": "integer", "description": "Integer to check"}},
            "required": ["n"],
        },
    },
}

# 17.
# Add a counter before the loop: tool_call_count = 0
# Increment inside the `for tool_call in msg.tool_calls:` block: tool_call_count += 1
# Print after the loop ends: print(f"Total tool calls: {tool_call_count}")

# 18.
last_call = None
for step in range(max_steps):
    ...
    for tool_call in msg.tool_calls:
        current_call = (tool_call.function.name, tool_call.function.arguments)
        if current_call == last_call:
            return "Stopped: repeated identical tool call detected."
        last_call = current_call
        ...

# 19.
try:
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
except Exception:
    return "Error: could not reach the model"

# 20.
def test_calculator_valid():
    assert calculator("2 + 2") == "4"

def test_calculator_invalid_chars():
    result = calculator("2 + import os")
    assert result.startswith("Error")
```
