# Security Policy

## Supported versions

| Version | Supported          |
| ------- | ------------------ |
| 0.4.x   | :white_check_mark: |
| 0.3.x   | :white_check_mark: |
| < 0.3   | :x:                |

## Reporting a vulnerability

Do **not** open a public issue for security bugs. Email the maintainer
at `security@quizgen.example` with:

- A description of the issue
- Reproduction steps
- Affected version(s)
- Any proof-of-concept payload

You'll get an acknowledgement within 72 hours and a fix ETA within 7 days.

## Scope

In scope:
- Remote code execution via crafted question banks (JSON/YAML import)
- Path traversal in the bank exporter
- Prompt-injection escapes that cause the LLM backend to execute
  local tooling
- Credential leaks from `config/secrets.toml`

Out of scope:
- Denial of service via deliberately huge banks (>1 GB) — the importer
  caps at 250 MB by design
- Social engineering of the maintainer
- Issues in third-party LLM providers

## Hardening notes

- All bank imports run through `quizgen/utils/sanitize.py` before parsing.
- LLM backends run in a subprocess with a 30s wall clock and no shell.
- The GUI never `eval()`s user content. Ever.