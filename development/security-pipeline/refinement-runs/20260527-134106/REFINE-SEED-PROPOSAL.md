# Refine Seed Proposal: Modular Security Pipeline

## Target

Define a reusable ResonantOS security pipeline abstraction that can host multiple security check families and allow checks to be added, removed, promoted, or deferred without rewriting the whole CI surface.

## Updated User Intent

The previous refinement focused on one supply-chain CI workflow. The refined target is broader:

- Create more than one security check over time.
- Define a whole pipeline abstraction only for security.
- Keep the checks modular and removable.
- Use supply-chain attack resistance as the MVP family.
- Produce an Invoke design artifact from the refined result.

## Source Context

- Active branch: `dev`.
- Existing alpha build workflow: `.github/workflows/alpha-build.yml`.
- Repo-local skill snapshots are available under `.codex/skills/`, so refinement and invoke work should use those skill files directly instead of requiring `tools/arcanum`.
- Existing supply-chain refinement result: `development/refinement-runs/20260527-131526/RESULT.md`.
- ResonantOS includes security-relevant domains beyond dependencies: Tauri host boundaries, provider secrets, add-on contracts, browser automation, audit logs, package distribution, and artifact provenance.

## Refined Problem

A single `security-supply-chain.yml` workflow is too narrow as the permanent architecture. It solves the MVP but does not give ResonantOS a place to grow security checks cleanly.

The better shape is:

> A security pipeline control plane that runs check modules by family, with supply chain as the first required family.

## Scope

Design-only in this run.

In scope:

- Security pipeline abstraction.
- Check family taxonomy.
- Check module contract.
- MVP supply-chain family.
- Add/remove/promotion rules.
- GitHub Actions integration shape.
- Invoke design bundle.

Out of scope:

- Implementing the workflow.
- Adding scanners or scripts.
- Enforcing branch protection.
- Packaging release attestations.

## Research Decision

`bounded-research`

Security CI guidance changes quickly. This run used a bounded current-source pass for GitHub dependency review, artifact attestations, OpenSSF Scorecard, npm provenance/signature behavior, and RustSec/cargo-audit framing.

## Done Criteria

This refinement is done when it produces:

- A refined final synthesis for the modular security pipeline.
- A design-ready abstraction with named modules, contracts, and gates.
- An Invoke design artifact with six required views.
- A supply-chain MVP definition that can become the first task-session implementation.

## Planned Stage Adaptation

Because this repo now carries local skill snapshots, command-backed stage ownership is interpreted through `.codex/skills/<skill>/SKILL.md` directly. The run does not require `tools/arcanum`.

Stages:

1. Context Builder evidence baseline: local skill-guided synthesis.
2. Invoke Define: represented by this seed and existing previous refinement result.
3. Interrogation refine-review: local critique recorded in manifest.
4. Research decision: bounded research completed.
5. Distill: smallest coherent unit selected.
6. Invoke Redefine / Design: materialized in `../../SECURITY-PIPELINE-DESIGN.md`.
7. Interrogation refine-design-review: local design review recorded in manifest.
8. Distill Repair: pipeline abstraction narrowed to control plane plus MVP family.
9. Invoke Plan: deferred; design mode only requested.
10. Final Interrogation and Synthesis: materialized in `RESULT.md`.
