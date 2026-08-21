# Python Best Practices

## Naming
- Use `snake_case` for functions and variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants.
- Avoid single-letter names except for loop counters or short lambdas.

## Functions
- Keep functions focused on a single responsibility. If a function needs a comment to explain "and then it also...", split it.
- Prefer explicit return values over relying on mutating arguments in place.
- Use type hints (`def foo(x: int) -> str:`) so callers and tools understand the contract.

## Error Handling
- Never use a bare `except:` — it silently swallows `KeyboardInterrupt` and real bugs. Catch specific exceptions.
- Don't use exceptions for normal control flow.
- Validate function inputs at the boundary (API handlers, file parsers), not everywhere internally.

## Common Pitfalls
- Mutable default arguments (`def f(items=[]):`) are shared across calls — use `None` and initialize inside the function.
- Comparing to `None`, `True`, `False` should use `is`, not `==`.
- Division by zero and `None` dereference are the most common runtime crashes — check inputs before using them.

## Structure
- Avoid deeply nested `if` blocks; prefer early returns (guard clauses).
- Avoid global mutable state; pass values explicitly.
- Keep files under ~300-400 lines where practical; split unrelated responsibilities into separate modules.
