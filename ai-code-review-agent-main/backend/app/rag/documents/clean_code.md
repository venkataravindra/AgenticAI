# Clean Code Principles

## Naming
- Names should reveal intent: `elapsed_time_ms` beats `t`. A reader shouldn't need to trace usage to understand a variable.
- Avoid disinformation: don't name a variable `list` if it's actually a dict; don't name a function `get_user` if it also writes to the database.

## Functions
- A function should do one thing. If you find yourself writing "and" when describing what it does, split it.
- Keep argument counts low (ideally ≤ 3). Long parameter lists are a sign the function is doing too much or needs a config object.
- Avoid boolean flag arguments that switch behavior (`def save(user, notify=True)`) — prefer two clearly named functions.

## Duplication (DRY)
- Repeated blocks of logic (not just repeated lines, but repeated *concepts*) should be extracted into a shared function.
- Don't over-apply DRY to code that looks similar but represents different business rules — that creates false coupling.

## Comments
- Good code explains itself through naming and structure. Comments should explain *why*, not *what* — a comment restating the code below it is noise.
- Delete commented-out dead code instead of leaving it "just in case" — version control already remembers it.

## Structure
- Prefer early returns / guard clauses over deeply nested conditionals.
- Keep related code close together; keep unrelated code apart (high cohesion, low coupling).
- Magic numbers/strings should be named constants, not scattered literals.
