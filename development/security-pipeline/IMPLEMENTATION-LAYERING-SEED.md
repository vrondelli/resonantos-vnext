# Implementation Layering Seed

## Layer 0: Skeleton

Goal: prove the pipeline abstraction can enumerate checks.

Potential outputs:

- `.github/security-pipeline/checks.yml`
- `scripts/security-pipeline/run-check.mjs`
- one no-op or lockfile adapter

Evidence:

- local command lists enabled checks
- disabled checks are skipped
- invalid registry fails clearly

## Layer 1: Supply Chain MVP

Goal: implement the first useful family.

Potential checks:

- `npm-lockfiles`
- `npm-audit`
- `rust-audit`
- `actions-hardening`
- GitHub dependency review job

Evidence:

- GitHub workflow runs on PR and `dev`
- high-risk supply-chain findings block
- warnings do not block until promoted

## Layer 2: Security Family Expansion

Goal: add non-supply-chain families without changing the core runner.

Candidate families:

- secrets
- Tauri boundary
- add-on boundary
- browser automation
- static analysis

Evidence:

- one new family can be added with a registry entry and adapter
- policy promotion is documented

## Layer 3: Release Integrity

Goal: connect security checks to alpha/release artifacts.

Candidate checks:

- SBOM generation
- artifact attestations
- provenance verification
- packaged artifact integrity

Evidence:

- release artifacts have provenance evidence
- security workflow and alpha build boundary remains clear
