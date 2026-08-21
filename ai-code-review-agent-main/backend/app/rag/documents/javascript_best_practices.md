# JavaScript / TypeScript Best Practices

## Variables
- Use `const` by default, `let` only when reassignment is needed. Never use `var` — it's function-scoped and causes hoisting bugs.
- Avoid implicit global variables (always declare with `const`/`let`).

## Equality
- Always use `===` and `!==` instead of `==`/`!=` to avoid type-coercion surprises (`"0" == false` is `true`).

## Async Code
- Always handle Promise rejections — an `async` function without a `try/catch` (or a `.catch()` on the caller) can crash the process or silently swallow errors.
- Avoid mixing `.then()` chains with `async/await` in the same function; pick one style.
- Never use `await` inside a loop when the calls are independent — use `Promise.all()` instead for performance.

## Functions & Structure
- Prefer small, named functions over large anonymous callbacks — easier to test and read stack traces.
- Avoid deeply nested callbacks ("callback hell"); use `async/await`.
- In TypeScript, avoid `any` — it defeats the purpose of the type system. Prefer `unknown` plus a type guard when the type is genuinely not known yet.

## Common Pitfalls
- Off-by-one errors in array loops (`<=` instead of `<`).
- Forgetting to `return` inside `.map()`/`.filter()` callbacks.
- Mutating props/state directly in React instead of creating a new object/array.
