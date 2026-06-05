# Installed Agent Skill Validation

Status: FLAG
Date: 2026-06-03
Strategy stages: installed-agent-skill-validation, malicious-skill-agent-audit

## Scope

This validation covers repository-local and generated agent capability surfaces:

- `.agents/skills`
- `.codex/skills`
- `.claude/skills`
- `.github/skills`
- `.claude/agents`
- `.github/copilot-instructions.md`
- `.github/instructions/arcanum.instructions.md`
- `tools/arcanum`
- `.codex/hooks*`
- dispatch-spec validator support files

## Evidence Commands

The current sandbox could execute approved `rg` commands, but shell-backed commands such as `git`, `sed`, and `python3` failed before launch with a missing `/bin/bash` process error. Validation therefore used static file discovery and pattern evidence only.

Observed commands:

```bash
rg --files -g 'SKILL.md' .agents .codex .claude .github/skills
rg --files .agents/formulae .codex/hooks .codex/hooks.json tools .agents/skills/dispatch-spec development/security-pipeline/research
rg -n '^name:|^description:|^allowed-tools:|canonical_source:|generated_by:|mutation_policy:' .agents .codex .claude .github/skills
```

## Findings

### F-001: Installed Skill Surfaces Exist

Verdict: PASS

The repository contains multiple installed skill surfaces with many `SKILL.md` manifests:

- `.agents/skills`
- `.codex/skills`
- `.claude/skills`
- `.github/skills`

The manifest scan found installed Arcanum skill packages such as `dispatch-spec`, `context-builder`, `task-session`, `x-ray`, `sigil-runtime-installer`, `spellcraft`, `inventory`, `refine`, `invoke`, and related generated aliases.

### F-002: Arcanum Runtime Entry Exists

Verdict: PASS

`tools/arcanum` exists and was included in the static audit scope. This gives the repository a concrete runtime/command surface to validate.

### F-003: Dispatch-Spec Validator Script Exists

Verdict: PASS

`.agents/skills/dispatch-spec/scripts/validate-dispatch.py` exists, and dispatch-spec fixture files exist under `.agents/skills/dispatch-spec/development/fixtures`.

### F-004: Repo-Local Dispatch Formulae Are Missing

Verdict: FLAG

The expected repo-local formulae path `.agents/formulae` is missing. That means a default repo-local dispatch validation route cannot rely on:

- `.agents/formulae/dispatch-spec/dispatch.schema.yml`
- `.agents/formulae/dispatch-spec/TECHNIQUE-CATALOG.md`

Earlier strategy work used an external canonical schema source. For this repository to validate dispatches deterministically without cross-repo assumptions, the schema/catalog lookup policy needs to be made explicit.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for dispatch-spec installed schema/catalog lookup support
```

### F-005: Codex Hook Surface Is Undecided Or Missing

Verdict: FLAG

The static scan did not find `.codex/hooks` or `.codex/hooks.json`, while installed runtime-installer skill documentation references legacy Codex hook surfaces. This may be valid if the current install profile intentionally uses native skills only, but it is not currently encoded as a validation decision.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for repo-local Arcanum hook surface validation
```

### F-006: Installed Surfaces Need Drift Validation

Verdict: FLAG

The repository has equivalent or near-equivalent capability packages across `.agents`, `.codex`, `.claude`, and `.github/skills`. Manual inspection is not sufficient to prove that aliases, generated metadata, canonical sources, mutation policies, and runtime instructions stay synchronized.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for installed skill surface drift validator
```

## Maturity Assessment

Installed skill/runtime validation is at Level 1: mapped.

It is not yet Level 2 because the repo-local schema/catalog source and hook-surface policy are not deterministically validated, and there is no automated drift checker across installed skill surfaces.

## Result

The installed agent skill validation stage is executable as a static audit, but not complete enough to mark mature. The next work should create deterministic validators for schema/catalog lookup, hook-surface policy, and cross-surface skill drift.
