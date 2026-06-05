# Task Session: Installed Skill Validation And Malicious Agent Audit

Date: 2026-06-03
Result: FLAG
Task-session scope: execute the first bounded security-agent strategy slice by validating installed agent skill/runtime surfaces and statically auditing for malicious skill/agent behavior.

## Context Pack

Inputs used:

- `development/security-pipeline/research/SECURITY-AGENT-RESEARCH-STRATEGY.md`
- `development/security-pipeline/research/security-agent-research.dispatch.json`
- `development/security-pipeline/research/security-agent-xray.html`
- repository-installed skill surfaces under `.agents`, `.codex`, `.claude`, and `.github/skills`
- `tools/arcanum`
- user instruction to use the development handoff rule whenever a development need is found

## Gate

Verdict: proceed with static validation only.

Reason: the current sandbox could run approved `rg` discovery commands, but shell-backed execution failed before launch due a missing `/bin/bash` process path. No dynamic validator or Python dispatch validation was rerun in this task-session.

## Execution

Completed:

- mapped installed skill surfaces
- checked for repo-local runtime entry points
- checked dispatch-spec validator presence
- checked expected hook/formulae support paths
- scanned installed skill manifests and `tools/arcanum` for hostile-content indicators
- created explicit development handoffs for every development-worthy gap

Generated artifacts:

- `development/security-pipeline/research/installed-agent-skill-validation.md`
- `development/security-pipeline/research/malicious-skill-agent-audit.md`

## Findings Summary

Installed skill validation:

- PASS: installed skill surfaces exist in `.agents`, `.codex`, `.claude`, and `.github/skills`.
- PASS: `tools/arcanum` exists.
- PASS: `.agents/skills/dispatch-spec/scripts/validate-dispatch.py` exists.
- FLAG: `.agents/formulae` is missing, so repo-local dispatch schema/catalog lookup is unresolved.
- FLAG: `.codex/hooks` and `.codex/hooks.json` are missing or intentionally absent, but the policy is not recorded.
- FLAG: cross-surface skill drift validation is not automated.

Malicious skill/agent audit:

- PASS: no direct private key material or obvious secret exfiltration payload was confirmed in observed scan output.
- FLAG: bootstrap skill documentation contains `curl | bash` style network-shell examples.
- FLAG: runtime adapter profiles in `tools/arcanum` need purpose-to-permission classification.
- FLAG: runtime local-write behavior needs a permission matrix.
- FLAG: hostile-content audit needs a deterministic scanner instead of manual pattern search.

## Required Development Handoffs

```text
$invoke handoff use context builder to prepare development for dispatch-spec installed schema/catalog lookup support
$invoke handoff use context builder to prepare development for repo-local Arcanum hook surface validation
$invoke handoff use context builder to prepare development for installed skill surface drift validator
$invoke handoff use context builder to prepare development for network-shell pattern allowlist for installed skills
$invoke handoff use context builder to prepare development for high-privilege runtime adapter policy classification
$invoke handoff use context builder to prepare development for runtime local-write permission matrix
$invoke handoff use context builder to prepare development for installed agent hostile-content scanner
```

## Validation

Deterministic validation completed:

- static file discovery with `rg --files`
- static manifest/provenance scan with `rg -n`
- hostile-content indicator scan with `rg -n`

Not completed:

- Python dispatch validator execution
- full recursive AST/data-flow audit
- build/test suite
- Git status verification

Reason: non-`rg` shell commands failed before execution in the current sandbox.

## Next Stage

Recommended next bounded task-session:

Create the `installed agent hostile-content scanner` context pack and implement a deterministic scanner that emits structured findings for network calls, command execution, secret handling, local writes, hook/persistence behavior, adapter privilege escalation, and allowed exceptions.
