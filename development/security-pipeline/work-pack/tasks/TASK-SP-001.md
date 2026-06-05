# TASK-SP-001: Define Security Check Registry

## Objective

Add the first declarative registry for security pipeline checks.

## Parent Layer

L0 Skeleton

## Source Contracts

- `development/security-pipeline/SECURITY-PIPELINE-DESIGN.md`
- `development/security-pipeline/IMPLEMENTATION-LAYERING.md`

## Write Scope

- `.github/security-pipeline/checks.yml`

## Implementation Detail

Create a versioned YAML registry with:

- top-level `version: 1`
- `families` map with `supply-chain` active
- `checks` list
- each check containing `id`, `family`, `policy`, `adapter`, and check-specific inputs
- policy values limited to `observe`, `warn`, `block`, `disabled`

Initial check entries:

- `npm-lockfiles`
- `npm-audit`
- `rust-audit`
- `actions-hardening`

Keep `dependency-review` in workflow config rather than the adapter registry unless a future adapter can run it locally.

## Smallest Working Units

### SWU-SP-001

- Goal: add `.github/security-pipeline/checks.yml` with the MVP supply-chain registry.
- Dependencies: none.
- Write scope: `.github/security-pipeline/checks.yml`.
- Done criteria: registry includes active `supply-chain` family and MVP check entries.
- Acceptance evidence: runner design can identify each adapter by id and family.
- Verification: later `node scripts/security-pipeline/run-check.mjs --list --config .github/security-pipeline/checks.yml`.
- Execution owner: local-fallback.
- Handoff note: keep schema minimal; do not invent non-MVP families as active checks.

## Expected Result Shape

```yaml
swu_id: SWU-SP-001
result: pass | flag | block | interrupted
files_touched:
  - .github/security-pipeline/checks.yml
validation:
  - registry list check or pending runner reason
blockers:
  - blocker or none
handoff_note: next SWU readiness
```
