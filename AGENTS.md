# Agent working boundary for this course

This repository is used for a software-engineering teaching exercise.

When asked to make changes during the course:

- Make only the changes relevant to the requested task.
- Avoid unrelated refactoring.
- Do not install packages or change dependencies without approval.
- Do not create, modify or delete automated tests unless explicitly requested.
- Do not stage, commit, push or open pull requests unless explicitly requested.
- Report unavailable tools rather than silently installing them.

The human participant should inspect the diff and decide what enters Git
history or the shared repository.

# Testing and verification

- Do not introduce new testing frameworks or dependencies.
- You may run existing tests to check for regressions.
- For implementation tasks, report how the changed behaviour can be
  verified manually.

When asked to write or modify tests, follow the specific instructions for
that task.

## Code quality

Follow the project's coding conventions.

Before completing a coding task:
- Run `ruff check .`
- Run `ruff format --check .`

Report any failures.