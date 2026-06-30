# Contributing to 30 Days of Agentic AI

First off, thank you for considering contributing! This project grows through
community effort, and every contribution — from fixing a typo to adding a
brand-new bonus project — genuinely helps thousands of learners.

## Ways to Contribute

- 🐛 **Report bugs** in code samples or instructions
- 📝 **Improve lessons** — clarify explanations, fix errors, add examples
- ✏️ **Add exercises or quiz questions**
- 🎨 **Improve diagrams** (Mermaid sources live inline in each `lesson.md`)
- 🚀 **Add a bonus project** to `projects/`
- 🌍 **Translate** a day's content into another language
- ✅ **Add tests** for existing code samples

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/<you>/30-Days-Agentic-AI.git`
3. Create a feature branch: `git checkout -b feat/day-12-improve-react-lesson`
4. Set up your environment:
   ```bash
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   ```
5. Make your changes
6. Run tests and linting:
   ```bash
   make lint
   make test
   ```
7. Commit using a clear message (see below)
8. Push and open a Pull Request against `main`

## Commit Message Convention

We use a simplified Conventional Commits style:

```
<type>(<scope>): <short description>

feat(day-09): add long-term memory persistence example
fix(day-14): correct chunking logic in RAG pipeline
docs(readme): fix broken curriculum links
test(day-22): add unit tests for coding agent
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

## Pull Request Guidelines

- Keep PRs focused on a single day/topic when possible
- Update the relevant `lesson.md`, `quiz.md`, or `cheatsheet.md` together if a
  concept changes
- Include or update tests for any code change in a `code/` folder
- Never delete reference solutions in `solutions/` without discussion
- Fill out the PR template completely

## Style Guide

- Code: PEP 8, formatted with `ruff format`
- Markdown: sentence-case headers, one topic per `##` section
- Diagrams: use Mermaid syntax, keep them under ~25 nodes for readability
- Keep explanations practical — favor a worked example over an abstract paragraph

## Adding a New Day Topic (maintainers only)

New days are only added via maintainer-approved proposals, since the 30-day
structure is intentionally fixed. Suggestions for new bonus days go in
`projects/` or `resources/` instead — open an issue first.

## Code of Conduct

By participating, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

Thank you for helping make this the best free agentic AI resource on GitHub! 🚀
