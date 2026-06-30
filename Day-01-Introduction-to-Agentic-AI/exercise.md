# Day 01 — Exercises

## Easy

1. In your own words (3–5 sentences), explain why a single ChatGPT prompt-completion
   is *not* an agent.
2. List three apps or products you use that you now believe contain agentic
   behavior, and identify which "level of agency" (0–4) each one operates at.
3. Draw (on paper or in Mermaid) the perceive-reason-act-observe loop from
   memory, without looking at the lesson.

## Medium

4. Modify `code/minimal_agent.py` so that `max_steps` defaults to `3` instead
   of `5`, then craft a prompt that would require more than 3 tool calls to
   answer correctly. Run it and observe what the agent returns when it hits
   the limit. Explain in a comment why this is dangerous behavior in a
   production system, and what you'd want to happen instead (preview of Day 26).
5. Add input validation to `calculator()` so that division by zero returns a
   clean error message (`"Error: division by zero"`) instead of crashing the
   program.
6. Write a second tool, `word_count(text: str) -> int`, register it in `TOOLS`
   and `AVAILABLE_FUNCTIONS`, and ask the agent a question that requires it
   (e.g., "How many words are in this sentence: ...?").

## Hard

7. **Debugging task:** The following modified loop has a bug that causes
   infinite repeated tool calls even when `max_steps` should stop it. Find
   and fix the bug:
   ```python
   for step in range(max_steps):
       response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
       msg = response.choices[0].message
       if msg.tool_calls:
           for tool_call in msg.tool_calls:
               result = AVAILABLE_FUNCTIONS[tool_call.function.name](**json.loads(tool_call.function.arguments))
               messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})
           continue
       return msg.content
   ```
   (Hint: compare carefully against the working version in `code/minimal_agent.py`.)

8. **Reasoning task:** Suppose you wanted the agent to refuse to answer
   questions unrelated to math entirely (e.g., reject "What's the capital of
   France?"). Would you implement this in the system prompt, as a guardrail
   function that runs before the LLM call, or both? Justify your answer in
   3–4 sentences, considering reliability.

## Open-Ended Design Question

9. Sketch (Mermaid or prose) the architecture for an agent that helps a user
   plan groceries for the week: it should check a recipe API, check what's
   already in the user's pantry (a database), and produce a shopping list.
   Identify which components from today's lesson (LLM, tools, memory,
   planner, orchestrator) this system needs, and which it could skip at a
   Level 2 implementation versus what it would need to reach Level 3.
