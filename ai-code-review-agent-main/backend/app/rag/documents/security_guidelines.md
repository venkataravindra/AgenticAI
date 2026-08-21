# Security Guidelines (AI-Assisted, Not a Full Audit)

## Secrets
- Never hardcode API keys, passwords, or tokens in source code. Use environment variables or a secrets manager.
- Flag any string literal that looks like a key (`sk-...`, `AKIA...`, long base64 blobs assigned to variables named `key`, `token`, `secret`, `password`).

## Input Handling
- Never build SQL queries with string concatenation or f-strings — use parameterized queries to prevent SQL injection.
- Never pass unsanitized user input to `eval()`, `exec()`, `os.system()`, `subprocess.run(..., shell=True)`, or JavaScript's `eval()`/`new Function()` — this enables command/code injection.
- Sanitize or escape user input before rendering it into HTML to prevent XSS (avoid `innerHTML` with raw user data, avoid `dangerouslySetInnerHTML`).

## Dangerous Operations
- File paths built from user input should be validated against path traversal (`../../etc/passwd`).
- Deserializing untrusted data with `pickle` (Python) or unsafe `yaml.load` (instead of `yaml.safe_load`) can execute arbitrary code.
- Disabling TLS/certificate verification (`verify=False`, `rejectUnauthorized: false`) should never ship to production.

## General
- Least privilege: don't request broader file/network/database permissions than the code needs.
- These are common AI-flaggable patterns, not a substitute for a real penetration test or a dedicated security review.
