# Refined Synthesis: Modular Security Pipeline

## Decision

Define a dedicated security pipeline abstraction for ResonantOS. Supply-chain checks are the MVP, but they should be implemented as the first check family inside a broader pipeline rather than as a one-off workflow.

## Smallest Coherent Unit

The smallest coherent unit is:

> A security pipeline control plane that discovers and runs modular check definitions, with supply-chain as the first required family.

This keeps the first implementation small while creating the structure needed to add secrets scanning, Tauri capability checks, add-on manifest checks, artifact provenance, and packaging hardening later.

## Pipeline Abstraction

### Security Pipeline

The top-level CI surface responsible for invoking security checks. It owns triggers, permissions, job isolation, reporting, and required-status behavior.

### Check Registry

A repo-owned configuration file that lists active checks, their family, scope, severity threshold, blocking mode, and adapter command.

Candidate path:

```text
.github/security-pipeline/checks.yml
```

### Check Adapter

A small script or command that executes one check consistently and reports status. Each adapter should be replaceable without changing the entire workflow.

Candidate path:

```text
scripts/security-pipeline/checks/<check-id>.mjs
```

### Check Family

A group of related checks that can be enabled as a unit. Families let ResonantOS grow security coverage without mixing unrelated policy decisions.

Initial families:

- `supply-chain`
- `secrets`
- `static-analysis`
- `tauri-boundary`
- `addon-boundary`
- `browser-automation`
- `provenance`
- `packaging`

### Check Policy

The rule that decides whether a finding blocks the pipeline, warns, or records advisory evidence.

Recommended policy modes:

- `block`: fail CI.
- `warn`: report but do not fail.
- `observe`: collect evidence only.
- `disabled`: known but inactive.

## MVP Family: Supply Chain

The first implementation should include only the minimum control plane plus these supply-chain modules:

| Check id | Purpose | Initial policy |
| --- | --- | --- |
| `npm-lockfiles` | fail when a dependency-bearing npm surface lacks a lockfile | block |
| `npm-audit` | run `npm ci --ignore-scripts` and high-severity audit per npm surface | block |
| `rust-audit` | run RustSec advisory checks against committed lockfiles | block |
| `dependency-review` | flag vulnerable dependency diff on pull requests | block for high/critical |
| `actions-hardening` | check workflow permissions, risky triggers, and action pinning policy | warn first, then block after baseline cleanup |

This MVP proves that checks can be added and removed by editing a registry and check adapter list instead of rewriting the entire workflow.

## Non-MVP Families

Defer these until the MVP pipeline is real:

- secret scanning and credential exposure checks
- Tauri capability and IPC boundary checks
- add-on manifest capability grant checks
- browser automation host boundary checks
- SAST or semgrep-style checks
- SBOM generation
- artifact attestations and SLSA provenance
- release package integrity checks

## Add/Remove Rule

A check is added by:

1. Creating or selecting an adapter.
2. Adding one registry entry.
3. Choosing a policy mode.
4. Adding validation evidence in the PR.

A check is removed or disabled by:

1. Changing policy to `disabled`, or deleting the registry entry.
2. Recording why it is removed.
3. Keeping the adapter if it may return later.

## Promotion Rule

Checks should move through:

```text
observe -> warn -> block
```

Supply-chain MVP checks can start at `block` where the repo already has enough deterministic evidence. `actions-hardening` should start as `warn` if the current `alpha-build.yml` needs action SHA pinning cleanup first.

## Design Result

Invoke design artifact:

```text
development/security-pipeline/SECURITY-PIPELINE-DESIGN.md
```

## Next Route

Invoke plan has now expanded this route into `development/security-pipeline/WORK-PACK.md`.

Use `task-session` for the MVP implementation:

1. Add the registry.
2. Add the runner/adapter skeleton.
3. Add supply-chain adapters.
4. Add the GitHub Actions workflow.
5. Run deterministic validation from `AGENTS.md`.

Recommended first execution unit:

```text
SWU-SP-001
```
