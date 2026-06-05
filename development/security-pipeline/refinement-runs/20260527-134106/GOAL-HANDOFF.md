# Goal Handoff: Modular Security Pipeline

## Objective

Create a modular CI security pipeline architecture for ResonantOS where each security check is a replaceable module, and the MVP implements the supply-chain family first.

## Recommended Next Route

`task-session` after design review.

The next route should implement only the MVP supply-chain family and the minimum pipeline skeleton needed to prove add/remove behavior.

## Target Implementation Boundary

Expected future files:

- `.github/workflows/security.yml`
- `.github/security-pipeline/checks.yml`
- `scripts/security-pipeline/run-check.mjs`
- `scripts/security-pipeline/checks/*.mjs`

Those paths are proposed, not created by this design run.

## First Implementation Principle

Do not encode every security concern directly in GitHub Actions YAML. Put stable orchestration in the workflow and move check definitions into a repo-owned security registry so new checks can be added by changing data plus one adapter.

## MVP

Supply-chain family:

- dependency lockfile presence
- npm install without lifecycle scripts
- npm audit threshold
- Rust advisory audit
- dependency review on pull requests
- GitHub Actions hardening policy

## Future Families

- secrets and credential exposure
- static application/security testing
- Tauri capability and IPC boundary checks
- add-on manifest and capability grant checks
- browser automation boundary checks
- artifact provenance, SBOM, and release integrity
- runtime/package hardening

## Validation For Next Execution

- `npm test -- --run`
- `npm run build`
- `cargo fmt --check && cargo test` from `src-tauri`
- JSON/YAML syntax checks for new pipeline config
- local dry run of registry enumeration and at least one check adapter
